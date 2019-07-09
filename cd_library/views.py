from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from cd_library.serializers.CDDescriptionSerializer import *
from cd_library.serializers.MusicTypesSerializer import *
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_403_FORBIDDEN


# Create your views here.
class CdDescriptionView(APIView):
    def get(self, request):

        cd_list = []
        queryset = CD.objects.all()
        for cd in queryset:
            cd_desc = DescriptionSerializer(cd).data
            cd_list.append(dict(cd_desc))

        return Response(cd_list, status=HTTP_200_OK)


class TypesView(viewsets.ModelViewSet):
    queryset = Types.objects.all()
    serializer_class = TypesSerializer
