from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from apps.book.api.serializers.partner_serializer import PartnerSerializer


class PartnerModelViewSet(viewsets.ModelViewSet):
    serializer_class = PartnerSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)

    @action(detail=False, methods=['get'], url_path='listpartner')
    def list_partner(self, request):
        dni_partner = request.data.get('dni', '')
        queryset = self.get_serializer().Meta.model.objects.filter(dni=dni_partner)
        partner_serializer = self.get_serializer(queryset, many=True)
        return Response(partner_serializer.data, status=status.HTTP_200_OK)


    def list(self, request):
        partner_serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(partner_serializer.data, status=status.HTTP_200_OK)


    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Socio registrado correctamente!'}, status=status.HTTP_201_CREATED)
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        partner = self.get_queryset().filter(id=pk).first()  # get instance
        if partner:
            partner.state = False
            partner.save()
            return Response({'message': 'Socio eliminado correctamente!'}, status=status.HTTP_200_OK)
        return Response({'error': 'No existe un Socio con estos datos!'}, status=status.HTTP_400_BAD_REQUEST)
