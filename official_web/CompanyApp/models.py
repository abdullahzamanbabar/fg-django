from django.db import models

# Create your models here.


class SliderImgs(models.Model):
    sliderImg = models.ImageField(upload_to="slider_imgs/")

class MemberInfo(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)

    GROUP_CHOICES = (
    ("Global", "Global"),
    ("Red", "Red"),
    ("Blue", "Blue"),
    ("Green", "Green"),
    )

    group = models.CharField(max_length=10, choices=GROUP_CHOICES, default=1)
    LinkedinURL = models.CharField(max_length=200, blank=True)
    picture = models.ImageField(upload_to="members_imgs/")