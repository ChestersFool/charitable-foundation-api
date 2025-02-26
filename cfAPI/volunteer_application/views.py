from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import VolunteerApplication
from .serializers import VolunteerApplicationSerializer
from user.models import User  # Імпортуємо модель користувача


class VolunteerApplicationAPIView(generics.ListAPIView):
    queryset = VolunteerApplication.objects.all()
    serializer_class = VolunteerApplicationSerializer


class VolunteerApplicationCreateView(APIView):
    def post(self, request):
        user_id = request.data.get('user')  # Отримуємо ID користувача
        try:
            user = User.objects.get(id=user_id)  # Отримуємо користувача
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        data = request.data.copy()

        serializer = VolunteerApplicationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
