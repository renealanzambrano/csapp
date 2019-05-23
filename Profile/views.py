#from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
# Create your views here.
from Profile.models import Profile
from Profile.serializers import ProfileSerializers

class ProfileList(APIView):
    def get(self,request,format=None):
        queryset= Profile.objects.filter(delete=False)
        serializer=ProfileSerializers(queryset,many=True,context= request)
        return Response(serializer.data)
        #Metodo para crear un nuevo registro
    def post(self,request,format=None):
            serializer=ProfileSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                datas=serializer.data
                return Response(datas,status=status.HTTP_201_CREATED)
class ProfileUpgrade(APIView):
    def get_object(self,pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            return "No existe el id"
        #Metodo para consiltar la id
    def get(self,request,pk,format=None):
        print("Este el id" + pk)
        Id=self.get_object(pk)
        if Id !="NO":
            Id= ProfileSerializers(Id)
            return Response(Id.data)
        
        return Response("No existe")
    #metodo para consultar la id y actualizar los campos
    def put(self,request,pk,format=None):
        Id= self.get_object(pk)
        serializer= ProfileSerializers(Id,data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas= serializer.data
            return Response(datas)
        return Response("Error",status=status.HTTP_400_BAD_REQUEST)


