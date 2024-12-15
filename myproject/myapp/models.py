from django.db import models

# Create your models here

class User(models.Model):
    email = models.EmailField(max_length = 30, unique= True)
    password = models.CharField(max_length=30)
    role = models.CharField(max_length=30)
    otp = models.IntegerField(default=456)
    created_at = models.DateField(auto_now=True)
    status = models.BooleanField(default= False)


class Chairman(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.TextField()
    contact_no = models.CharField(max_length=15)
    pic = models.FileField(upload_to='media/images/',default='media/defaultpic.webp')


class Member(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.TextField()
    contact_no = models.CharField(max_length=15)


class Notice(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    description = models.TextField()
    pic = models.FileField(upload_to='media/images/',default='media/noticeDefault.png')
    created_at = models.DateField(auto_now=True)

