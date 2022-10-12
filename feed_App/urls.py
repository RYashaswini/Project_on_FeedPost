from django.urls import path
from feed_App.views import *
from knox import views as knox_views

urlpatterns=[
    
    path('create_user/', UserCreate.as_view()),
    path('update_user/<int:pk>/', UserUpdate.as_view()),

    path('create_post/',PostCreate.as_view()),
    path('update_post/<int:pk>/',PostUpdate.as_view()),

    
    path('create_postnn/',PostCreateNN.as_view()),
    path('update_postnn/<int:pk>/',PostUpdateNN.as_view()),

    path('login/', LoginView.as_view()),

    path('adminpost/',AdminPostStatus.as_view()),    

    path('approvestatus/',ApprovePostStatus.as_view()),

    path('rejectstatus/',RejectPostStatus.as_view()),

    path('actionstatus/',ActionStatus.as_view()),

    path('wholedata/',WholeData.as_view()), 
    path('wholedata/<int:pk>/',WholeDataUpdate.as_view()), 

    path('logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),

    path('pagedata/',PageData.as_view()), 
    path('pagedata/<int:pk>/',PageData.as_view()), 



   

]