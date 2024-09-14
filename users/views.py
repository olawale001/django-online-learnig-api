from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from .models import CustomUser
from .serializers import RegisterSerializer, LoginSerializer

class RegisterView(generics.CreateAPIView, generics.ListCreateAPIView, generics.DestroyAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer
    parser_classes = [MultiPartParser, FormParser]


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    parser_classes = [MultiPartParser, FormParser]    

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })

