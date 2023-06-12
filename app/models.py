from operator import mod
from pyexpat import model
from statistics import mode
from django.db import models
import uuid


class ProfileUser(models.Model):
    uid = models. UUIDField(default=uuid.uuid4, editable=False, primary_key=True)

    name = models.CharField(max_length=1009)

    photo= models.ImageField(upload_to='profile')
    def str(self) -> str:
        return self.name



class Status(models.Model):
    user= models.ForeignKey(ProfileUser, on_delete=models.CASCADE,related_name='status')
    file =models.ImageField(upload_to='status')
    
    
class post(ProfileUser):
    user=models.ImageField(upload_to='pro')