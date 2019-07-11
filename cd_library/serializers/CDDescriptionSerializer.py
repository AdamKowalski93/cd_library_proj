from rest_framework import serializers
from cd_library.models.CdDescription import *
from cd_library.serializers.MusicTypesSerializer import *


class DescriptionSerializer(serializers.ModelSerializer):
    cd_music_type = serializers.SerializerMethodField(method_name='get_cd_type')

    @staticmethod
    def get_cd_type(cd):
        types = []
        get_object_type = cd.type.get_queryset()
        for object in get_object_type:
            cd_type = TypesSerializer(object).data
            types.append(dict(cd_type))

        return types

    class Meta:
        model = CD
        fields = ('title', 'description', 'artist', 'date', 'cd_music_type')
