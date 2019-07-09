from rest_framework import serializers
from cd_library.models.CdDescription import *
from cd_library.serializers.MusicTypesSerializer import *


class DescriptionSerializer(serializers.ModelSerializer):
    type_value = TypesSerializer(source='type', many=True)


    class Meta:
        model = CD
        fields = ('title', 'description', 'artist', 'date', 'type_value')
