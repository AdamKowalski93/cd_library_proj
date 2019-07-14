from rest_framework import serializers
from cd_library.models.CdDescription import *
from cd_library.serializers.MusicTypesSerializer import *


class DescriptionSerializer(serializers.ModelSerializer):
    music_type_string = serializers.SerializerMethodField(method_name='get_cd_type')

    def get_cd_type(self,cd):
        return cd.type.type

    # @staticmethod
    # def get_cd_type(cd):
    #     types = []
    #     get_object_type = cd.type.get_queryset()
    #     for object in get_object_type:
    #         cd_type = TypesSerializer(object).data
    #         types.append(dict(cd_type))

        # return types

    class Meta:
        model = CD
        fields = ('id','title', 'description', 'artist', 'date', 'type','music_type_string')
