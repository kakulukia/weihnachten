from django.contrib.admin.models import LogEntry
from rest_framework import serializers

from events.models import Event
from flea_market.models import MarketInquiry


class InquirySerializer(serializers.ModelSerializer):

    class Meta:
        model = MarketInquiry
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'phone',
            'permanent_seller',
            'chosen',
            'blocked',
            'canceled',
            'email_valid',
            'event'
        ]
        read_only_fields = [
            'id',
            'chosen',
            'blocked',
            'canceled',
            'email_valid'
        ]

    def validate(self, attrs):
        if MarketInquiry.data.filter(event_id=attrs['event'], email=attrs['email']).exists():
            raise serializers.ValidationError("Diese E-Mail-Adresse ist bereits registriert.")
        return attrs


class FleaMarketEventSerializer(serializers.ModelSerializer):
    inquiries = InquirySerializer(many=True)
    tables_taken = serializers.SerializerMethodField()
    max_tables = serializers.SerializerMethodField()
    available_inquiries = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = [
            'start',
            'id',
            'inquiries',
            'tables_taken',
            'max_tables',
            'available_inquiries',
            'cancel_date',
        ]

    def get_tables_taken(self, obj):
        return obj.inquiries.filter(chosen=True, canceled=False).count()

    def get_max_tables(self, obj):
        return 29

    def get_available_inquiries(self, obj):
        return obj.inquiries.available().count()


class LogSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='short_name', read_only=True)
    change_message = serializers.SerializerMethodField()

    class Meta:
        model = LogEntry
        fields = [
            'action_time',
            'user',
            'change_message',
        ]

    def get_change_message(self, obj):
        return obj.get_change_message()
