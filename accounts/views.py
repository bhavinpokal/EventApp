from django.shortcuts import render
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import UserSerializer


class UserRegistrationAPIView(APIView):
    """
    Handles user registration
    """

    template_name = "accounts/register.html"

    def get(self, request):
        """
        Returns Register HTML template
        """
        return render(request, self.template_name)

    def post(self, request):
        """
        On POST request, creates user
        """
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            refresh = RefreshToken.for_user(serializer.instance)
            return Response(
                {"access": str(refresh.access_token), "refresh": str(refresh)},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginAPIView(APIView):
    """
    Provides user login view
    """

    renderer_classes = [TemplateHTMLRenderer]
    template_name = "accounts/login.html"

    def get(self, request):
        return Response(template_name=self.template_name)
