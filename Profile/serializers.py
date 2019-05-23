from rest_framework import routers,serializers,viewsets
#NombreApp       d                   Nombre modelo
from Profile.models import Profile
#from drf_dynamic_fields import DynamicFieldsMixin
class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model= Profile
        fields=('name','ap_pat','ap_mat','year','img')

#class ProfileSerializers2(serializers.ModelSerializer):
    #class Meta: