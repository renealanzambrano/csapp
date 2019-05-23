from rest_framework import routers,serializers,viewsets

from Cliente.models import Cliente

class ClienteSerializers(serializers.ModelSerializer):
    class Meta:
        model= Cliente
        fields= ('__all__')