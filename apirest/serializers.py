from rest_framework import serializers
from apirest.models import Sensores, Lecturas

class SensoresSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sensores
        fields = ('id', 'temperatura', 'humedad', 'peso')

class LecturasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecturas
        fields = ('id', 'key', 'value', 'date_created')
