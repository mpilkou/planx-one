from uuid import uuid4
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import URLValidator


import string
from django.utils.crypto import get_random_string
def generate_short_url_string():
    return get_random_string(6, string.ascii_uppercase + string.digits + string.ascii_lowercase)

# Create your models here.
class URL(models.Model):
    sourse_url = models.URLField(max_length=1000, blank=False, validators=(URLValidator, ))
    short_url = models.CharField(max_length=6, blank=False, unique=True, db_index=True, default=generate_short_url_string)
    user = models.ForeignKey(User, blank=False, on_delete=models.CASCADE)

    def save(self, *args, **kwargs) -> None:
        while URL.objects.filter(short_url=self.short_url).exists():
            self.short_url = generate_short_url_string()
        return super().save(*args, **kwargs)