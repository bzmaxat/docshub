from django.db import models

from users.models import User


class Document(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)
    file = models.FileField(upload_to="uploads/")
    created = models.DateTimeField(auto_now_add=True)
    initiator = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name
