
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from .serializers import LoginSerializer, RegisterSerializer
from rest_framework import status


class LoginAPIView(ObtainAuthToken, APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        return Response({'token': token.key})


class RegisterAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(status=status.HTTP_202_ACCEPTED)

        elif serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_202_ACCEPTED)

