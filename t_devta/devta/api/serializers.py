from rest_framework import serializers
from devta.models import news

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = news
        fields = ('heading','content','date')
