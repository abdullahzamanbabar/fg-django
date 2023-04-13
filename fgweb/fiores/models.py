from django.db import models
from image_cropping import ImageRatioField
import os

# Create your models here.
class SliderImgs(models.Model):
    sliderImg = models.ImageField(upload_to="slider_imgs/")
    cropping = ImageRatioField('sliderImg', '1080x1080', allow_fullsize=True, free_crop=True)

    def delete(self, *args, **kwargs):
        os.remove(self.sliderImg.path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return str(self.sliderImg)

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=1000)
    message = models.TextField(blank=True, verbose_name='Message (Optional)')
    cv = models.FileField(upload_to="cvs/", max_length=300)

    def delete(self, *args, **kwargs):
        os.remove(self.cv.path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.name+"-"+self.email


class Members(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)

    choices = (
    ("Leadership", "Leadership"),
    ("Red Group", "Red Group"),
    ("Blue Group", "Blue Group"),
    ("City", "City"),
)

    group =  models.CharField(max_length=200, choices=choices, default='1')
    linkedin =  models.CharField(max_length=200)
    photo = models.ImageField(upload_to="members/")
    cropping = ImageRatioField('photo', '650x650', free_crop=True)

    my_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
        db_index=True,
    )

    class Meta:
        ordering = ['my_order']

    def delete(self, *args, **kwargs):
        os.remove(self.photo.path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.name+"-"+self.position

class Projects(models.Model):
    title = models.CharField(max_length=200)
    logo = models.ImageField(upload_to="projects/")
    description = models.TextField()
    projecturl =  models.CharField(max_length=200, blank=True, verbose_name='Project Url (Optional)')
    image1 = models.ImageField(upload_to="projects/")
    image2 = models.ImageField(upload_to="projects/")
    croppinglogo = ImageRatioField('logo', '650x650', allow_fullsize=True, free_crop=True)
    croppingimage1 = ImageRatioField('image1', '1080x1080', allow_fullsize=True, free_crop=True)
    croppingimage2 = ImageRatioField('image2', '1080x1080', allow_fullsize=True, free_crop=True)

    def delete(self, *args, **kwargs):
        os.remove(self.logo.path)
        os.remove(self.image1.path)
        os.remove(self.image2.path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.title