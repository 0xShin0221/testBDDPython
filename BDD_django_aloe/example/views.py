from rest_framework.generics import ListAPIView
from .models import Friendship
from .serializers import UserSerializer


class FriendsView(ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return Friendship.objects.friends(self.request.user)