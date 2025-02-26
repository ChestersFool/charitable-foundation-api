from django.db import models


class VolunteerApplication(models.Model):
    id = models.AutoField(primary_key=True)  # Автоінкрементний унікальний ідентифікатор
    user = models.ForeignKey("user.User", on_delete=models.CASCADE, null=True)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)  # Дата створення заявки
    status = models.CharField(
        max_length=50,
        choices=[
            ("pending", "Очікує розгляду"),
            ("in_progress", "В обробці"),
            ("resolved", "Вирішено"),
        ],
        default="pending",
    )

    def str(self):
        return f"Запит #{self.id} - {self.status}"