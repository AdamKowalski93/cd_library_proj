from rest_framework import serializers
from cd_library.models.MusicTypes import *


class TypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Types
        fields = [('type')]




