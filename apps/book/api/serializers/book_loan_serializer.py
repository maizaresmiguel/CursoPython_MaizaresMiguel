from apps.book.models import Bookloan

from rest_framework import serializers

class BookLoanSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bookloan
        exclude = ('state','created_date','modified_date','deleted_date')

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'status': instance.status,
            'book': instance.book.name if instance.book.name is not None else '',
            'partner': instance.partner.first_name if instance.partner.first_name is not None else '',
        }