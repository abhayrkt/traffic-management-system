from rest_framework.generics import ListAPIView,RetrieveAPIView
from devta.models import news
from .serializers import NewsSerializer

class NewsListView(ListAPIView):
    queryset = news.objects.all()
    serializer_class = NewsSerializer


class NewsDetailView(RetrieveAPIView):
    queryset = news.objects.all()
    serializer_class = NewsSerializer

    
