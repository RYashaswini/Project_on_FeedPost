from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email' , 'password','is_superuser']
        extra_kwargs= {
            'password' : {'write_only' : True}
        }
    
    def create(self, validated_data):
        user = User.objects.create(
        email = validated_data['email'],
        username = validated_data['username'],
        password = make_password(validated_data['password'])
        )
        return user
    
    def get_username(self, name):
        name = User.objects.filter(username=name)
        if name.exists():
            raise serializers.ValidationError("username is already taken")
        return name

    # def validate(self,data):
    #     if data.get('username'):
    #         a=data.get('username')
    #         user_qs=User.objects.filter(username=a)
    #         if user_qs.exists():
    #             raise ValidationError({'username':'Username is already taken'})
    #     if data.get('username'):
    #         b=data.get('username')
    #         if (b == ""):
    #             raise ValidationError({'username':'Username should not be empty'})
    #     if data.get('email'):
    #         d=data.get('email')
    #         if (d == ""):
    #             raise ValidationError({'email':'Email should not be empty'})
    #     if data.get('password'):
    #         c=data.get('password')
    #         if (c == ""):
    #             raise ValidationError({'password':'Password should not be empty'})
    #     return data

class PostSerializer(serializers.ModelSerializer):
    user_id = UserSerializer()
    
    class Meta:
        model = PostModel
        fields = ['post_id', 'post_name', 'upload_image' ,'upload_date', 'description','status','reason','user_id']

    # def validate(self,data):
    #     if data.get('post_name'):
    #         post_name=data.get('post_name')
    #         if (post_name == ""):
    #             raise serializers.ValidationError({'post_name':'Post name should not be empty'})
    #     if data.get('post_name'):
    #         post_name=data.get('post_name')
    #         user_qs=PostModel.objects.filter(post_name=post_name)
    #         if user_qs.exists():
    #             raise ValidationError({'post_name':'Post name already exists'})
    #     return data


class PostSerializerNN(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields = ['post_id', 'post_name', 'upload_image' , 'description','upload_date','status','reason','user_id']

class WholeDataSerializer(serializers.ModelSerializer):
    post_details = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'post_details', 'date_joined']

    def get_post_details(self, obj):
        data = PostModel.objects.filter(user_id=obj.id).values()
        return data

