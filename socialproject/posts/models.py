from django.db import models
from django.conf import settings
# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    subject = models.CharField(max_length=20)
    description = models.CharField(max_length=250)
    created = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.subject