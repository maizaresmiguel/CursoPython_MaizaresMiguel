from apps.book.models import Author

from rest_framework import serializers

class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        exclude = ('state','created_date','modified_date','deleted_date')