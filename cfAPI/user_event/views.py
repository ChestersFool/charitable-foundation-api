from rest_framework import generics, status
from rest_framework.response import Response
from user_event.models import UserEvent
from .serializers import UserEventSerializer
from user.models import User  # Імпортуємо модель користувача


class UserAPIView(generics.ListAPIView):
    queryset = UserEvent.objects.all()
    serializer_class = UserEventSerializer


class RegisterForEventView(generics.CreateAPIView):
    def post(self, request):
        user_id = request.data.get('user')  # Отримуємо ID користувача
        try:
            user = User.objects.get(id=user_id)  # Отримуємо користувача
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        data = request.data.copy()

        serializer = UserEventSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)