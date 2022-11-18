from apps.book.models import Partner

from rest_framework import serializers

class PartnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Partner
        exclude = ('state','created_date','modified_date','deleted_date')