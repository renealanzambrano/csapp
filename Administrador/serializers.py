from rest_framework import routers,serializers,viewsets
#NombreApp       d                   Nombre modelo
from Administrador.models import Administrador

class  AdministradorSerializers(serializers.ModelSerializer):
    class Meta:
        model=Administrador
        fields= ('id','name','ap_mat','ap_pat','year','img')