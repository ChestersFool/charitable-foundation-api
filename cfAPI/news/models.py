from django.db import models


class News(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    publication_time = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=2000)
    author = models.CharField(max_length=255)

    def __str__(self):
        return self.title
