from django.shortcuts import render
from django.contrib.auth.models import User
from genric_app import serializers
from genric_app.serializers import UserSerializer ,ReviewSerializer 
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .models import *
from rest_framework.response import Response


class UserList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
    
    
    
    def list(self, request):
        queryset = self.get_queryset()
        serializer = UserSerializer(self.filter_queryset(self.get_queryset()), many=True, context={"request": request})
        return Response(serializer.data)

    def get_queryset(self):
        user = self.request.user
        return Book.objects.all()
    
    
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

class BookView(APIView):
    def get(self, request):
        b = Book.objects.all()
        serializer = UserSerializer(b, many=True)
        return Response({"articles": serializer.data})
    


class RetrieveDeleteItem(GenericAPIView):

    serializer_class = UserSerializer
    queryset = Book.objects.all()

    # def get(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance)
    #     return Response(serializer.data)

    # def delete(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     instance.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
    
    # def get(self, request, *args, **kwargs):
    #     """
    #     Method for Post listing. It can be accessed by anyone.
    #     """

    #     import pdb;pdb.set_trace()
    #     serializer = UserSerializer(self.filter_queryset(self.get_queryset()), many=True, context={"request": request})

    #     return Response(serializer.data)
    
    
    def filter_queryset(self, queryset):
        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, self)
        return queryset
    
    
# class UserListAPIView(generics.ListAPIView):
#     """

#     """
#     queryset = User.objects.filter(is_admin=False, is_staff=False, is_superuser=False).exclude(status=4)

#     filter_backends = [SearchFilter, OrderingFilter]
#     search_fields = ['name', 'publish_date', 'author']
#     #pagination_class = UserPageNumberPagination

#     class Meta:
#        ordering = ['-id']

#     def get_serializer_class(self):
#         if self.request.user.is_superuser:
#             return UserSerializer
#         else:
#             return UserSerializer

#     serializer_class = get_serializer_class()  # this is the line 59    
    
from rest_framework.permissions import IsAuthenticatedOrReadOnly
    
    
class ProfessorReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    
    def get_queryset(self):
        queryset = super(ProfessorReviewList, self).get_queryset()
        return queryset.filter(professor__pk=self.kwargs.get('pk'))

    permission_classes = (IsAuthenticatedOrReadOnly,
                         )

    def perform_create(self, serializer):
        # The request user is set as author automatically.
        serializer.save(author=self.request.user) 


from rest_framework import mixins, generics
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from .models import Book
from genric_app.serializers import UserSerializer


class MyCustomAPIView(mixins.ListModelMixin, 
                      mixins.CreateModelMixin,
                    #   mixins.DestroyModelMixin,
                    #   mixins.UpdateModelMixin,
                    #   mixins.RetrieveModelMixin,
                      generics.GenericAPIView):

    queryset = Book.objects.all()
    serializer_class = UserSerializer
   
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    # def get(self, request, *args, **kwargs):
    #     return self.retrieve(request, *args, **kwargs)

    # def delete(self, request, *args, **kwargs):
    #     return self.destroy(request, *args, **kwargs)   
    
    
class BookListView(RetrieveUpdateDestroyAPIView):    
    serializer_class=UserSerializer
    
    def get_queryset(self):
        queryset=Book.objects.filter(name=self.request.name)
        return queryset
    
    
#concreate view classes--------------------            