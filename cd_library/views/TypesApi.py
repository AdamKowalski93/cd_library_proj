from django.http import Http404
from rest_framework.views import APIView

from cd_library.serializers.MusicTypesSerializer import *
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_403_FORBIDDEN
from rest_framework import status


class Type(APIView):

    def get(self, request, type_id):
        type_list = []
        queryset = Types.objects.get(id=type_id)
        type_obj = TypesSerializer(queryset).data
        type_list.append(dict(type_obj))
        return Response(type_list, status=HTTP_200_OK)

    def post(self, request):
        serializer = TypesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, type_id):
        query = Types.objects.get(id=type_id)
        serializer = TypesSerializer(query, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, type_id):
        query = Types.objects.get(id=type_id)
        query.delete()
        return Response
