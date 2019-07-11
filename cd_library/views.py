from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from cd_library.serializers.CDDescriptionSerializer import *
from cd_library.serializers.MusicTypesSerializer import *
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_403_FORBIDDEN
from rest_framework import generics
from rest_framework import status


# Create your views here.
class CdDescriptionView(APIView):
#class CdDescriptionView(viewsets.ModelViewSet):

    # queryset = CD.objects.all()
    # serializer_class = DescriptionSerializer

    def get(self, request):
        cd_list = []
        queryset = CD.objects.all()
        for cd in queryset:
            cd_desc = DescriptionSerializer(cd).data
            cd_list.append(dict(cd_desc))

        return Response(cd_list, status=HTTP_200_OK)

    def post(self, request):
        serializer = DescriptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TypesView(viewsets.ModelViewSet):
    queryset = Types.objects.all()
    serializer_class = TypesSerializer
