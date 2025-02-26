from django.db import models


class HelpRequest(models.Model):
    id = models.AutoField(primary_key=True)  # Автоінкрементний унікальний ідентифікатор
    user = models.ForeignKey("user.User", on_delete=models.CASCADE, null=True)
    description = models.TextField()  # Опис проблеми
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

    def __str__(self):
        return f"Запит #{self.id} - {self.status}"
