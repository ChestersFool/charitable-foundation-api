from rest_framework import serializers
from .models import VolunteerApplication


class VolunteerApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VolunteerApplication
        fields = ['id', 'user', 'content', 'date', 'status']
        read_only_fields = ['id', 'date', 'status']  # Дата та статус будуть встановлюватися автоматично
