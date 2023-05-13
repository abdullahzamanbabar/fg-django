from django.db import models
import os

# Create your models here.

class LogoBackgroundImgs(models.Model):
    header_footer_color = models.CharField(max_length=200, blank=True, verbose_name='Header & Footer Color (linear gradient) -- (optional)')
    swiper_text = models.CharField(max_length=200, blank=True, verbose_name='Swiper Text -- (optional)')
    swiper_color = models.CharField(max_length=200, blank=True, verbose_name='Swiper Color (linear gradient) -- (optional)')
    swiper_text_color = models.CharField(max_length=200, blank=True, verbose_name='Swiper Text Color -- (optional) ')
    logo = models.ImageField(upload_to="background_imgs/", blank=True, verbose_name='Logo -- (optional)')
    personalImg = models.ImageField(upload_to="background_imgs/", blank=True, verbose_name='Personal Image -- (optional)')
    blobColor = models.CharField(max_length=100, blank=True, verbose_name='Blob Color: (linear gradient) -- (optional)')
    backgroundImg= models.ImageField(upload_to="background_imgs/", blank=True, verbose_name='BackgroundImg -- (Optional)')
    contactImg = models.ImageField(upload_to="background_imgs/", blank=True, verbose_name='ContactImg -- (Optional)')
    contact_heading = models.CharField(max_length=100, blank=True, verbose_name='Contact Form Heading -- (optional)')
    contact_label_color = models.CharField(max_length=200, blank=True, verbose_name='Contact Form Labels Color -- (optional)')

    def delete(self, *args, **kwargs):
        if self.logo.name:      # check if logo field has a file
            os.remove(self.logo.path)
        if self.personalImg.name:
            os.remove(self.personalImg.path)
        if self.backgroundImg.name:
            os.remove(self.backgroundImg.path)
        if self.contactImg.name:
            os.remove(self.contactImg.path)
        super().delete(*args, **kwargs)

    # def __str__(self):
    #     return str(self.header_footer_color)

class PersonalInfo(models.Model):
    text_color = models.CharField(max_length=200, blank=True, verbose_name='Text Color -- (optional)')
    info = models.TextField(help_text='Accpets HTML tags and inline styling', verbose_name='Personal Info')
    
    # def __str__(self):
    #     return str(self.info)[:10]

class CV(models.Model):
    buttonText = models.CharField(max_length=50, blank=True, verbose_name='Download Button Text -- (optional)')
    button_text_color = models.CharField(max_length=200, blank=True, verbose_name='Button Text Color -- (optional)')
    button_color = models.CharField(max_length=200, blank=True, verbose_name='Button Color -- (optional)')
    addfile = models.FileField(upload_to="files/", blank=True, max_length=300, verbose_name='Upload File -- (optional)')

    def delete(self, *args, **kwargs):
        if self.addfile.name:
            os.remove(self.addfile.path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return str(self.addfile)

class SwiperStack(models.Model):
    swiperImgs = models.ImageField(upload_to="swiper_imgs/",verbose_name='Add a Swiper Img')

    def delete(self, *args, **kwargs):
        os.remove(self.swiperImgs.path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return str(self.swiperImgs)

class Groups(models.Model):
    group_name = models.CharField(max_length=100, verbose_name='Group Name')
    group_color = models.CharField(max_length=200, blank=True, verbose_name='Group Color (linear gradient) -- (optional)')
    group_text_color = models.CharField(max_length=200, blank=True, verbose_name='Group Text Color -- (optional)')
    front_card_color = models.CharField(max_length=200, blank=True, verbose_name='Front Card Color (linear gradient) -- (optional)')
    front_card_text_color = models.CharField(max_length=200, blank=True, verbose_name='Front Card Text Color -- (optional)')
    back_card_color = models.CharField(max_length=200, blank=True, verbose_name='Back Card Color (linear gradient) -- (optional)')
    back_card_text_color = models.CharField(max_length=200, blank=True, verbose_name='Back Card Text Color: (Hex Code) -- (optional)')

    def __str__(self):
        return str(self.group_name)

class CareerInfo(models.Model):
    group_name = models.ForeignKey(Groups, on_delete=models.CASCADE)
    front_card = models.TextField(help_text='Accpets HTML tags and inline styling', verbose_name='Front Card Info')
    back_card = models.TextField(help_text='Accpets HTML tags and inline styling', blank=True ,verbose_name='Back Card Info -- (optional)')


    def __str__(self):
        return str(self.group_name)+' CareerInfo'[:10]

class Contact(models.Model):
    name = models.CharField(max_length=200, verbose_name='Name')
    email = models.EmailField(max_length=200, verbose_name='Email')
    message = models.TextField(verbose_name='Message')

    def __str__(self):
        return self.name+"-"+self.email

class FooterIcons(models.Model):
    footerIcon = models.CharField(max_length=50, help_text='Visit https://fontawesome.com/ (Use free fontawesome classnames: e.g. fa-brands fa-linkedin)' , verbose_name='Social Media Icon')
    IconUrl = models.CharField(max_length=200, verbose_name='Social Medial Url')
    IconColor = models.CharField(max_length=200, verbose_name='Icon Color')
    hoverColor = models.CharField(max_length=20,verbose_name='Icon Color on hover')

    def __str__(self):
        return str(self.footerIcon)

class Projects(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    url = models.CharField(max_length=1000, blank=True, verbose_name='URL -- (optional)')
    image = models.ImageField(upload_to="project_imgs/")

    def delete(self, *args, **kwargs):
        os.remove(self.image.path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return str(self.title)

