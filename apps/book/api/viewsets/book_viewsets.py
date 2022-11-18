from django.db.models import Q
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from apps.book.models import Author

from apps.book.api.serializers.book_serializer import BookSerializer


class BookModelViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)

    def list(self, request):
        book_serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(book_serializer.data, status=status.HTTP_200_OK)


    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Book registrada correctamente!'}, status=status.HTTP_201_CREATED)
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


    def update(self, request, pk=None):
        if self.get_queryset(pk):
            # send information to serializer referencing the instance
            book_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)
            if book_serializer.is_valid():
                book_serializer.save()
                return Response({'message': 'Book actualizado correctamente!'}, status=status.HTTP_200_OK)
            return Response({'message': '', 'error': book_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        book= self.get_queryset().filter(id=pk).first()  # get instance
        if book:
            book.state = False
            book.save()
            return Response({'message': 'Book eliminado correctamente!'}, status=status.HTTP_200_OK)
        return Response({'error': 'No existe un Book con estos datos!'}, status=status.HTTP_400_BAD_REQUEST)


    @action(detail=False, methods=['get'], url_path='listauthorbook')
    def list_author_name(self, request):
        last_name = request.data.get('last_name', '')
        first_name = request.data.get('first_name', '')
        authorfind = Author.objects.filter(
            Q(last_name__iexact=last_name) &
            Q(first_name__iexact=first_name)).first()
        queryset = self.get_serializer().Meta.model.objects.filter(author=authorfind)
        book_serializer = self.get_serializer(queryset, many=True)
        return Response(book_serializer.data, status=status.HTTP_200_OK)
