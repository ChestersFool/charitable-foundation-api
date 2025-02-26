from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username_tg = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
