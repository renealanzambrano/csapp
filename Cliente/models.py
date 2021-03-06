#from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Cliente(models.Model):
    name= models.CharField(max_length=100,null=False)
    ap_pat=models.CharField(max_length=100,null=False)
    ap_mat=models.CharField(max_length=100,null=False)
    year= models.IntegerField(null=False)
    delete= models.BooleanField(default=False)
    created=models.DateTimeField(default=timezone.now)
    edited= models.DateTimeField(blank=True,null=True,default=None)

    def _str_(self):
        return self.name

    class Meta:
        db_table='Cliente'