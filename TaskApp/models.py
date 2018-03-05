from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, Model, ForeignKey, CASCADE


class CustomUser(AbstractUser):
    country = CharField(max_length=128, null=True)


class Image(Model):
    file_name = CharField(max_length=100)
    extension = CharField(max_length=5)
    path = CharField(max_length=500)
    user = ForeignKey(CustomUser, on_delete=CASCADE)
