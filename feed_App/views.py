
from msilib.schema import ListView
from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics 
from rest_framework.views import APIView  
from rest_framework.response import Response 
from rest_framework import status
from django.contrib.auth import login
from django.contrib.auth.models import User 
from rest_framework.pagination import PageNumberPagination
from django.core.paginator import Paginator 
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import permissions,filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from knox.auth import TokenAuthentication

class UserCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class UserUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PostCreate(generics.ListCreateAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer
    
class PostUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer

class PostCreateNN(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,) 
    
    queryset = PostModel.objects.all()
    serializer_class = PostSerializerNN
    
class PostUpdateNN(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,) 
    
    queryset = PostModel.objects.all()
    serializer_class = PostSerializerNN

class AdminPostStatus(generics.ListCreateAPIView):
    queryset = PostModel.objects.filter(status__isnull = True).all()
    serializer_class = PostSerializer 

class ApprovePostStatus(generics.ListCreateAPIView):
    approve = "Approved"
    queryset = PostModel.objects.filter(status = approve).all()
    serializer_class = PostSerializer

class RejectPostStatus(generics.ListCreateAPIView):
    reject = "Rejected"
    queryset = PostModel.objects.filter(status = reject).all()
    serializer_class = PostSerializer

class ActionStatus(generics.ListCreateAPIView):
    queryset = PostModel.objects.exclude(status__isnull = True).all()
    serializer_class = PostSerializer 
    filter_backends = [filters.OrderingFilter]
 




class WholeData(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = WholeDataSerializer
    # authentication_classes = (TokenAuthentication,)
    # pagination_class = PageNumberPagination
    
class WholeDataUpdate(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = WholeDataSerializer
#     authentication_classes = (TokenAuthentication,)
#     pagination_class = PageNumberPagination

    # def get_object(self, id):
    #     try:
    #         return User.objects.get(id = id)
    #     except User.DoesNotExist:
    #         return User(status=status.HTTP_400_BAD_REQUEST)

    # def get(self,request, id):
    #     user = User.get_object(id)
    #     serializer = WholeDataSerializer(user,many=True)
    #     pagination_class = PageNumberPagination
    #     return Response(serializer.data)

# class WholeDataUpdate(generics.ListAPIView):
#     model=User
#     paginate_by=5
#     paginator_class=Paginator
    
#     def get_context_data(self,**kwargs):
#         context=super().get_context_data(**kwargs)
#         page=self.request.GET.get('page',1)
#         users=User.objects.all.order_by('id')
#         paginator=self.paginator_class(users,self.paginate_by)

#         users=paginator.page(page)
#         context['users']=users
#         return context
    
    


  

class LoginView(KnoxLoginView):
    permission_classes = (permissions.AllowAny,) 

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginView, self).post(request, format=None)


class PageData(generics.ListAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    pagination_class = PageNumberPagination
