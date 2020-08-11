from rest_framework import serializers
from .models import news

class devtaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devta
        fields = ('heading','content')
