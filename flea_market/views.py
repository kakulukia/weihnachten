import pendulum
from django.http import HttpResponse
from rest_framework.decorators import action

from .models import Event
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import ModelViewSet

from flea_market.models import Inquiry
from flea_market.serialzers import EventSerializer, InquirySerializer


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


class EventsViewSet(ModelViewSet):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    queryset = Event.data.all()
    serializer_class = EventSerializer

    @action(detail=True, methods=['get'], url_path='download')
    def download(self, request, pk):

        event = self.get_object()
        response = HttpResponse(content_type="application/pdf")
        response.write(event.get_pdf())
        response['Content-Disposition'] = 'inline; filename="%s"' % "Gästeliste.pdf"

        return response


class InquiryViewSet(ModelViewSet):
    http_method_names = ['post']
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    queryset = Inquiry.data.all()
    serializer_class = InquirySerializer


class SubmitMarketInquiryView(CreateModelMixin, GenericAPIView):
    permission_classes = []
    serializer_class = InquirySerializer

    def post(self, request):
        response = self.create(request)
        return response
