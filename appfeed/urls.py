from django.urls import path
from appfeed import views

urlpatterns=[
    path('',views.register,name='register' ),
    path('signin/',views.signin,name='signin' ),

    path('addpost/',views.addpost,name="addpost"),
    path('addpost/',views.addpost,name="addpost"),
    
    path('retrieve/',views.retrieve,name="retrieve"),
    path('addstatus/<int:post_id>/',views.addstatus,name="addstatus"),

    path('feedpost/',views.feedpost,name="feedpost"),

    path('signout/',views.user_logout,name='signout')

]