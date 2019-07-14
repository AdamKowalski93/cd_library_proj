from django.http import Http404
from rest_framework.views import APIView

from cd_library.serializers.CDDescriptionSerializer import *
from cd_library.serializers.MusicTypesSerializer import *
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_403_FORBIDDEN
from rest_framework import status


class Cd(APIView):

    def get(self, request, cd_id):
        cd_list = []
        queryset = CD.objects.get(id=cd_id)
        cd_desc = DescriptionSerializer(queryset).data
        cd_list.append(dict(cd_desc))
        return Response(cd_list, status=HTTP_200_OK)

    def post(self, request):
        serializer = DescriptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, cd_id):
        query = CD.objects.get(id=cd_id)
        serializer = DescriptionSerializer(query, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, cd_id):
        query = CD.objects.get(id=cd_id)
        query.delete()
        return Response
