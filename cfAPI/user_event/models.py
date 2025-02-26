from django.db import models


class UserEvent(models.Model):
    id = models.AutoField(primary_key=True)  # Автоінкрементний унікальний ідентифікатор
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='user_events')
    event = models.ForeignKey('event.Event', on_delete=models.CASCADE, related_name='event_users')
    registration_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'event')
        ordering = ['-registration_date']

    def __str__(self):
        return f"{self.id}"
