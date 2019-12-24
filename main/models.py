from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class PostModel(models.Model):
    post=models.CharField(max_length=256)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now=True)
    #date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.post)
class Friend(models.Model):
    users=models.ManyToManyField(User)
    current_user=models.ForeignKey(User,related_name='owner',null=True,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.users)
    @classmethod
    def make_friend(cls,current_user,new_friend):
        friend,created=cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.add(new_friend)
    @classmethod
    def lose_friend(cls,current_user,new_friend):
        friend,created=cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.remove(new_friend)