from django.db import models
from django.contrib import auth


class User(auth.models.User, auth.models.PermissionsMixin):
    def __str__(self):
        return "@{}".format(self.username)


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<identifier>
    return 'user_{0}/{1}.png'.format(instance.user.id, instance.identifier)


class Assets(models.Model):
    image = models.ImageField(blank=True, null=True, upload_to=user_directory_path)
    options = (('uploaded', 'UPLOADED'),
               ('archived', 'ARCHIVED'),)
    status = models.CharField(max_length=100, choices=options)
    message = models.CharField(max_length=200)
    downloadURL = models.URLField(max_length=200)

    def __str__(self):
        return self.status
