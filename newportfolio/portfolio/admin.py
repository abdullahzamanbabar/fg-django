from django.contrib import admin
import os

from portfolio.models import LogoBackgroundImgs, SwiperStack, FooterIcons, CV, PersonalInfo, Groups, CareerInfo, Contact, Projects

# Register your models here.
class LogoBackgroundImgsAdmin(admin.ModelAdmin):
    
    def delete_queryset(self, request, queryset):
        for obj in queryset:
            if obj.logo.name:       # check if logo field has a file
                os.remove(obj.logo.path)
            if obj.personalImg.name:
                os.remove(obj.personalImg.path)
            if obj.backgroundImg.name:
                os.remove(obj.backgroundImg.path)
            if obj.contactImg.name:
                os.remove(obj.contactImg.path)
        super().delete_queryset(request, queryset)

class CVAdmin(admin.ModelAdmin):

    def delete_queryset(self, request, queryset):
        for obj in queryset:
            if obj.addfile.name:
                os.remove(obj.addfile.path)
        super().delete_queryset(request, queryset)

class SwiperStackAdmin(admin.ModelAdmin):

    def delete_queryset(self, request, queryset):
        for obj in queryset:
            os.remove(obj.swiperImgs.path)
        super().delete_queryset(request, queryset)

class ProjectsAdmin(admin.ModelAdmin):

    def delete_queryset(self, request, queryset):
        for obj in queryset:
            os.remove(obj.image.path)
        super().delete_queryset(request, queryset)


admin.site.register(LogoBackgroundImgs, LogoBackgroundImgsAdmin)
admin.site.register(PersonalInfo)
admin.site.register(CV, CVAdmin)
admin.site.register(SwiperStack, SwiperStackAdmin)
admin.site.register(Groups)
admin.site.register(CareerInfo)
admin.site.register(Contact)
admin.site.register(FooterIcons)
admin.site.register(Projects, ProjectsAdmin)