import pendulum
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

    # @action(detail=True, methods=['post'], url_path='draw-tables')
    # def draw_tables(self, request, pk):
    #     event = self.get_object()
    #     event.draw_tables()
    #     event.add_log_entry(request.user, 'Tische verlost')
    #     return Response()


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
