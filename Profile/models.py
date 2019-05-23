from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Profile(models.Model):
    name= models.CharField(max_length=100,null=False)
    ap_pat=models.CharField(max_length=100,null=False)
    ap_mat=models.CharField(max_length=100,null=False)
    year= models.IntegerField(null=False)
    img= models.ImageField(upload_to='media/',null=True,blank=True)
    delete= models.BooleanField(default=False)
    created=models.DateTimeField(default=timezone.now)
    edited= models.DateTimeField(blank=True,null=True,default=None)

    def _str_(self):
        return self.pk

    class Meta:
        db_table='Profile'

class Profile2(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET(-1))
    address= models.CharField(max_length=250, null= False)
    
