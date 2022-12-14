from django.db import models
from rest_framework import serializers

# Create your models here.


def Artists_Profile_Images(instance, filename):
    return '/'.join(['Media_Files', 'Artists_Profile_Images', str(instance.artist_name) + "_" + str(filename)])


class ArtistsModel(models.Model):

    class Meta:
        ordering = ['id']

    artist_name = models.CharField(null=False, blank=True, max_length=256)
    artist_profileImage = models.ImageField(
        null=False, blank=True, upload_to=Artists_Profile_Images)

    def __str__(self):
        return f"{self.pk}: {self.artist_name}"


class ArtistsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtistsModel
        fields = '__all__'
