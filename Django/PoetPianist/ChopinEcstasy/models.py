from django.db import models
from django.contrib.auth.models import Group, Permission, User



class UserProfile(models.Model):
    # Your existing fields

    groups = models.ManyToManyField(Group, related_name='user_profiles', blank=True)
    user_permissions = models.ManyToManyField(
        Permission, related_name='user_profiles', blank=True
    )

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Change this line

    def __str__(self):
        return self.title