from rest_framework import serializers
from . import models

class Bank_ser(serializers.ModelSerializer):
    class Meta:
        model = models.Bankdata
        fields = '__all__'




