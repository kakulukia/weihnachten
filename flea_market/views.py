import codecs
import os
import pendulum
# Create your views here.
from constance import config
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.views.generic.base import View
from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import action
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from events.models import Event
from events.views import CsrfExemptSessionAuthentication
from flea_market.models import MarketInquiry
from flea_market.serialzers import FleaMarketEventSerializer, InquirySerializer, LogSerializer


class FleaMarketEventsViewSet(ModelViewSet):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    queryset = Event.data.flea_market().filter(
            start__gt=pendulum.now().start_of('day'))
    serializer_class = FleaMarketEventSerializer

    @action(detail=True, methods=['post'], url_path='draw-tables')
    def draw_tables(self, request, pk):
        event = self.get_object()
        event.draw_tables()
        event.add_log_entry(request.user, 'Tische verlost')
        return Response()

    @action(detail=True, methods=['get'], url_path='download')
    def download(self, request, pk):

        event = self.get_object()
        response = HttpResponse(content_type="application/pdf")
        response.write(event.get_sellers_list())
        response['Content-Disposition'] = 'inline; filename="%s"' % "Verkäuferliste.pdf"

        return response


class MarketOverview(LoginRequiredMixin, TemplateView):
    template_name = 'flea_market/market_management.pug'
    extra_context = {"has_permission": True}


class PDFTestView(View):
    def get(self, request):
        event = Event.data.get(id=798)
        with codecs.open(os.path.join(settings.BASE_DIR, 'assets/css/pdf.css'), 'r') as css:
            styles = css.read()

        return render(request, 'pdf/seller_list.pug', {'event': event, 'styles': styles})


class InquiryViewSet(ModelViewSet):
    http_method_names = ['post']
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    queryset = MarketInquiry.data.valid()
    serializer_class = InquirySerializer

    @action(detail=True, methods=['post'])
    def choose(self, request, pk):
        inquiry = self.get_object()
        inquiry.accept()

        inquiry.event.add_log_entry(request.user, f'{inquiry.name} wurde akzeptiert.')

        return Response()

    @action(detail=True, methods=['post'])
    def block(self, request, pk):
        inquiry = self.get_object()
        inquiry.blocked = not inquiry.blocked
        inquiry.save()

        if inquiry.blocked:
            inquiry.event.add_log_entry(request.user, f'{inquiry.name} wurde geblockt.')
        else:
            inquiry.event.add_log_entry(request.user, f'Blockade von {inquiry.name} wurde aufgehoben.')

        return Response()

    @action(detail=True, methods=['post'])
    def cancel(self, request, pk):
        inquiry = self.get_object()
        inquiry.cancel()

        inquiry.event.add_log_entry(request.user, f'{inquiry.name} wurde abgesagt.')

        return Response()

    @action(detail=True, methods=['post'])
    def validate(self, request, pk):
        inquiry = self.get_object()
        inquiry.validate_email()
        return Response()

    @action(detail=True, methods=['post'], url_path='make-permanent')
    def make_permanent(self, request, pk):
        inquiry = self.get_object()
        inquiry.make_permanent(request.data['yes_no'])

        if inquiry.permanent_seller:
            inquiry.event.add_log_entry(request.user, f'{inquiry.name} wurde als Dauergast markiert.')
        else:
            inquiry.event.add_log_entry(request.user, f'{inquiry.name} ist nicht länger Dauergast.')

        return Response()


class CancelMarketInquiryView(APIView):
    permission_classes = []

    def post(self, request, token):

        inquiry = get_object_or_404(MarketInquiry, token=token)

        context = {
            'user': " ".join([inquiry.first_name, inquiry.last_name]),
        }
        status = 200
        if pendulum.now().add(days=config.MARKET_CANCEL_DURATION) < pendulum.instance(inquiry.event.start):
            inquiry.canceled = True
            inquiry.save()
        else:
            status = 400

        return Response(status=status, data=context)


class ValidateEmailView(APIView):
    permission_classes = []

    def post(self, request, token):

        inquiry = get_object_or_404(MarketInquiry, token=token)
        inquiry.validate_email()

        return Response()


class MarketLogsView(APIView):
    def get(self, request, event_id):
        event = get_object_or_404(Event, id=event_id)
        return Response(LogSerializer(event.get_logs(), many=True).data)


class CurrentMarketEventView(APIView):
    permission_classes = []

    def get(self, request):
        current_market = Event.data.current_flea_market()
        return Response(FleaMarketEventSerializer(current_market).data)


class NextMarketEventView(APIView):
    permission_classes = []

    def get(self, request):
        next_market = Event.data.next_flea_market()
        return Response(FleaMarketEventSerializer(next_market).data)



class SubmitMarketInquiryView(CreateModelMixin, GenericAPIView):
    permission_classes = []
    serializer_class = InquirySerializer

    def post(self, request):
        response = self.create(request)
        return response
