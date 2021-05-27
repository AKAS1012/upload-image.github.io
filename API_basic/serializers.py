from rest_framework import serializers
from .models import Assets


class AssetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assets
        fields = ['id', 'image', 'status', 'message', 'downloadURL']



