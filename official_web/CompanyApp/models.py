from django.db import models
from django.core import validators

# Create your models here.


class SliderImgs(models.Model):
    sliderImg = models.ImageField(upload_to="slider_imgs/",verbose_name='SliderImg (1100x500)')

    def __str__(self):
        return str(self.sliderImg)

class Groups(models.Model):
    group_name = models.CharField(max_length=200)
    text = models.TextField()
    picture = models.ImageField(upload_to="team_imgs/", verbose_name='Group Picture (255x255)')
    
    def __str__(self):
        return self.group_name

class MemberInfo(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)

    group_name = models.ForeignKey(Groups, on_delete=models.CASCADE)
    LinkedinURL = models.CharField(max_length=200, blank=True, verbose_name='LinkedinURL (Oprional)')
    picture = models.ImageField(upload_to="members_imgs/", verbose_name='Member Picture (310x323)')
    
    def __str__(self):
        return self.name+"-"+self.position+"-"+str(self.group_name)

class Story(models.Model):
    title = models.CharField(max_length=300)
    text = models.TextField()
    
    def __str__(self):
        return self.title

class HomeColumn2(models.Model):
    title = models.CharField(max_length=300)
    text = models.TextField()
    
    def __str__(self):
        return self.title

class About(models.Model):
    title = models.CharField(max_length=300)
    text = models.TextField()
    
    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=400)
    text = models.TextField()
    picture = models.ImageField(upload_to="project_imgs/", verbose_name='ProjectImg (537x269)')
    
    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, validators=[
        validators.EmailValidator()])
    message = models.TextField()

    def __str__(self):
        return self.name+"-"+self.email

class FooterText(models.Model):
    textTop = models.CharField(max_length=300,verbose_name='TextTop')
    textBottom = models.CharField(max_length=300, blank=True, verbose_name='TextBottom (Optional)')
        
    def __str__(self):
        return self.textTop[:20]

class FooterIcon(models.Model):
    icon = models.ImageField(upload_to="social_imgs/", verbose_name='SocialMedia Icon (32x32)')
    iconUrl = models.CharField(max_length=500, verbose_name='Icon URL')

    def __str__(self):
        return self.iconUrl[:20]