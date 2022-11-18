from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from apps.book.api.serializers.author_serializer import AuthorSerializer


class AuthorModelViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)



    @action(detail=False, methods=['get'], url_path='listadoapellidos')
    def list_last_name(self, request):
        author = request.data.get('last_name', '')
        queryset = self.get_serializer().Meta.model.objects.filter(last_name=author)
        author_serializer = self.get_serializer(queryset, many=True)
        return Response(author_serializer.data, status=status.HTTP_200_OK)


    def list(self, request):
        author_serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(author_serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Author registrado correctamente!'}, status=status.HTTP_201_CREATED)
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        author = self.get_queryset().filter(id=pk).first()  # get instance
        if author:
            author.state = False
            author.save()
            return Response({'message': 'Author eliminado correctamente!'}, status=status.HTTP_200_OK)
        return Response({'error': 'No existe un Author con estos datos!'}, status=status.HTTP_400_BAD_REQUEST)


    def update(self, request, pk=None):
        if self.get_queryset(pk):
            # send information to serializer referencing the instance
            author_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)
            if author_serializer.is_valid():
                author_serializer.save()
                return Response({'message': 'author actualizado correctamente!'}, status=status.HTTP_200_OK)
            return Response({'message': '', 'error': author_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

