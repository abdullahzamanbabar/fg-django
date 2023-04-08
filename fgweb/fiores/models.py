from django.db import models

# Create your models here.
class SliderImgs(models.Model):
    sliderImg = models.ImageField(upload_to="slider_imgs/")

    def __str__(self):
        return str(self.sliderImg)

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=1000)
    message = models.TextField()
    cv = models.FileField(upload_to="cvs/", max_length=300)

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

    def __str__(self):
        return self.name+"-"+self.position

class Projects(models.Model):
    title = models.CharField(max_length=200)
    logo = models.ImageField(upload_to="projects/")
    description = models.TextField()
    projecturl =  models.CharField(max_length=200, blank=True, verbose_name='Project Url (Optional)')
    image1 = models.ImageField(upload_to="projects/")
    image2 = models.ImageField(upload_to="projects/")

    def __str__(self):
        return self.title