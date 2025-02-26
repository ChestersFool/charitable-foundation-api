from rest_framework import serializers
from .models import HelpRequest


class HelpRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = HelpRequest
        fields = ['id', 'user', 'description', 'date', 'status']
        read_only_fields = ['id', 'date', 'status']  # Дата та статус будуть встановлюватися автоматично
