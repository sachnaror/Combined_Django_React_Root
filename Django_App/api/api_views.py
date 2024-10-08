from Django_App.models import Book
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import (authentication_classes,
                                       permission_classes)
from rest_framework.permissions import IsAuthenticated

from .serializers import BookSerializer


class ListBooksAPI(generics.ListAPIView):
    authentication_classes=[ SessionAuthentication ]
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.response import Response
from rest_framework.views import APIView

ensure_csrf = method_decorator(ensure_csrf_cookie)
class setCSRFCookie(APIView):
    permission_classes = []
    authentication_classes = []
    @ensure_csrf
    def get(self, request):
        return Response("CSRF Cookie set.")


from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_protect
from rest_framework.permissions import AllowAny

from .serializers import LoginSerializer

csrf_protect_method = method_decorator(csrf_protect)
class LoginView(APIView):
    permission_classes = (AllowAny,)
    authentication_classes = ()
    @csrf_protect_method
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response("Logged in")






