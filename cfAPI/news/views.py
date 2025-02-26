from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import News
from .serializers import NewsSerializer


class NewsAPIView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class NewsDetailView(APIView):
    def get(self, request, news_id):
        try:
            news = News.objects.get(id=news_id)  # Отримуємо новину за ID
        except News.DoesNotExist:
            return Response({"error": "News not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = NewsSerializer(news)
        return Response(serializer.data, status=status.HTTP_200_OK)
