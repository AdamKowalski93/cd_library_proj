from rest_framework.views import APIView

from cd_library.serializers.CDDescriptionSerializer import *
from cd_library.serializers.MusicTypesSerializer import *
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_403_FORBIDDEN
from rest_framework import status


class TypesView(APIView):

    def get(self, request):
        types_list = []
        queryset = Types.objects.all()
        for type in queryset:
            type = TypesSerializer(type).data
            types_list.append(dict(type))

        return Response(types_list, status=HTTP_200_OK)
