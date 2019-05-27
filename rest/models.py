from django.db import models
from .choices import CHOICE
from .lang import LANG
# Create your models here.
class NewUser(models.Model):
    name=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    profession=models.CharField(choices=CHOICE,max_length=20,default='',blank=True)
    language=models.CharField(choices=LANG,max_length=20,blank=True)
    pro=models.BooleanField(default=False)
    def __str__(self):
        return self.name
