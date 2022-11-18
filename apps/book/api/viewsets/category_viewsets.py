from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from apps.book.api.serializers.category_serializer import CategorySerializer


class CategoryModelViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)

    @action(detail=False, methods=['get'], url_path='listcategory')
    def list_category(self, request):
        name_category = request.data.get('name', '')
        queryset = self.get_serializer().Meta.model.objects.filter(name=name_category)
        category_serializer = self.get_serializer(queryset, many=True)
        return Response(category_serializer.data, status=status.HTTP_200_OK)


    def list(self, request):
        category_serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(category_serializer.data, status=status.HTTP_200_OK)


    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Categoria registrado correctamente!'}, status=status.HTTP_201_CREATED)
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        category = self.get_queryset().filter(id=pk).first()  # get instance
        if category:
            category.state = False
            category.save()
            return Response({'message': 'Categoria eliminada correctamente!'}, status=status.HTTP_200_OK)
        return Response({'error': 'No existe una Categoria con estos datos!'}, status=status.HTTP_400_BAD_REQUEST)
