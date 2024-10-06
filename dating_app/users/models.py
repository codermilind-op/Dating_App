from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    age = models.IntegerField(null=True, blank=True)
    interests = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=100, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)

    liked_users = models.ManyToManyField('self', symmetrical=False, related_name='liked_by',blank=True)
    disliked_users = models.ManyToManyField('self', symmetrical=False, related_name='disliked_by',blank=True)
    matches = models.ManyToManyField('self', symmetrical=False, related_name='matched_with')

    def __str__(self):
        return f'{self.user.username} Profile'


# from django.contrib.auth.models import User
# from django.db import models
# #
# # class UserProfile(models.Model):
# #     user = models.OneToOneField(User, on_delete=models.CASCADE)
# #     bio = models.TextField(max_length=500, blank=True)
# #     age = models.IntegerField(null=True, blank=True)
# #     location = models.CharField(max_length=100, blank=True)
# #     profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
#
#     # Tracking who the user liked and who liked the user
#     liked_users = models.ManyToManyField('self', symmetrical=False, related_name='liked_by')
#     disliked_users = models.ManyToManyField('self', symmetrical=False, related_name='disliked_by')
#     matches = models.ManyToManyField('self', symmetrical=False, related_name='matched_with')
#
#     def __str__(self):
#         return f'{self.user.username} Profile'
from django.db import models
from django.contrib.auth.models import User

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Notification for {self.user.username}: {self.message}'
