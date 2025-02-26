from rest_framework import serializers
from .models import UserEvent


class UserEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserEvent
        fields = ['user', 'event', 'registration_date']
        read_only_fields = ['registration_date']

    def validate(self, data):
        user = data.get('user')
        event = data.get('event')

        # Перевіряємо, чи вже існує такий запис (оскільки unique_together)
        if UserEvent.objects.filter(user=user, event=event).exists():
            raise serializers.ValidationError("Користувач вже зареєстрований на цей івент.")

        return data
