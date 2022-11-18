from apps.book.models import Book
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        exclude = ('state','created_date','modified_date','deleted_date')

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name,
            'isbn': instance.isbn,
            'category': instance.category.name if instance.category.name is not None else '',
            'author': instance.author.first_name if instance.author.first_name is not None else '',
        }

