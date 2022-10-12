from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class PostModel(models.Model):
    post_id = models.AutoField(primary_key=True)
    post_name = models.CharField(max_length=100)
    upload_image = models.ImageField(upload_to='media/',null=True,blank=True)
    description = models.CharField(max_length=1000)
    upload_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=100,null=True,blank=True)
    reason = models.CharField(max_length=100,null=True,blank=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.post_name




