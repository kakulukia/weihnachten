from rest_framework import serializers

from flea_market.models import Inquiry
from .models import Event


class InquirySerializer(serializers.ModelSerializer):

    class Meta:
        model = Inquiry
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'phone',
            'class_name',
            'kids',
            'adults',
            'event',
        ]
        read_only_fields = [
            'id',
        ]

    def validate(self, attrs):
        if attrs['kids'] + attrs['adults'] > attrs['event'].available_places:
            raise serializers.ValidationError(
                f'An diesem Tag können max. {attrs["event"].available_places} Plätze gebucht werden.')

        return attrs


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = [
            'start',
            'id',
            'for_schools',
            'available_places',
        ]
