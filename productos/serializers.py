from rest_framework import serializers
from .models import Chela


class ChelaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chela
        #especificamso que debe serializar todos los fields del modelo
        fields = '__all__'