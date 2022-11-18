from django.db.models import Q
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from apps.book.models import Author

from apps.book.api.serializers.book_loan_serializer import BookLoanSerializer


class BookLoanModelViewSet(viewsets.ModelViewSet):
    serializer_class = BookLoanSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)

    def list(self, request):
        book_loan_serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(book_loan_serializer.data, status=status.HTTP_200_OK)


    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Prestamo registrado correctamente!'}, status=status.HTTP_201_CREATED)
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk=None):
        book_loan= self.get_queryset().filter(id=pk).first()  # get instance
        if book_loan:
            book_loan.state = False
            book_loan.save()
            return Response({'message': 'Prestamo eliminado correctamente!'}, status=status.HTTP_200_OK)
        return Response({'error': 'No existe un Prestamo con estos datos!'}, status=status.HTTP_400_BAD_REQUEST)


    @action(detail=False, methods=['get'], url_path='listbookloan')
    def loan_name(self, request):
        dni = request.data.get('dni', '')
        dnifind = Author.objects.filter(
            Q(dni__iexact=dni)).first()
        queryset = self.get_serializer().Meta.model.objects.filter(author=dnifind)
        book_serializer = self.get_serializer(queryset, many=True)
        return Response(book_serializer.data, status=status.HTTP_200_OK)
