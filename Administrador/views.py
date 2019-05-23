from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

# Create your views here.
from Administrador.models import Administrador
from Administrador.serializers import AdministradorSerializers

class AdministradorList(APIView):
    def get(self,request,format=None):
        queryset= Administrador.objects.filter(delete=False)
        serializer=AdministradorSerializers(queryset,many=True)
        return Response(serializer.data)
        #Metodo para crear un nuevo registro
    def post(self,request,format=None):
            serializer=AdministradorSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                datas=serializer.data
                return Response(datas,status=status.HTTP_201_CREATED)
    #def put(self,request,pk,format=None):
        #administrador= Administrador.objects.get(pk=pk)
        #serializer= AdministradorSerializers(administrador,data=request.data)
        #if serializer.is_valid():
            #serializer.save()
            #datas=serializer.data
            #return Response(datas,status=status.HTTP_201_CREATED)
class AdministradorUpgrade(APIView):
    #Para consultar el id y decir que no existe el id consultado
    def get_object(self,pk):
        try:
            return Administrador.objects.get(pk=pk)
        except Administrador.DoesNotExist:
            return "No existe el id"
        #Metodo para consiltar la id
    def get(self,request,pk,format=None):
        print("Este el id" + pk)
        Id=self.get_object(pk)
        if Id !="NO":
            Id= AdministradorSerializers(Id)
            return Response(Id.data)
        
        return Response("No existe")
    #metodo para consultar la id y actualizar los campos
    def put(self,request,pk,format=None):
        Id= self.get_object(pk)
        serializer= AdministradorSerializers(Id,data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas= serializer.data
            return Response(datas)
        return Response("Error",status=status.HTTP_400_BAD_REQUEST)
        
 
