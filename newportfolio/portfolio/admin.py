from django.contrib import admin
import os

from portfolio.models import LogoBackgroundImgs, SwiperStack, FooterIcons, CV, PersonalInfo, Groups, CareerInfo, Contact

# Register your models here.
class LogoBackgroundImgsAdmin(admin.ModelAdmin):
    list_display = ['swiper_text', 'contact_heading']

    def delete_queryset(self, request, queryset):
        for obj in queryset:
            os.remove(obj.logo.path)
            os.remove(obj.personalImg.path)
            os.remove(obj.backgroundImg.path)
            os.remove(obj.contactImg.path)
        super().delete_queryset(request, queryset)

class CVAdmin(admin.ModelAdmin):
    list_display = ['buttonText', 'button_color']

    def delete_queryset(self, request, queryset):
        for obj in queryset:
            os.remove(obj.addfile.path)
        super().delete_queryset(request, queryset)

class SwiperStackAdmin(admin.ModelAdmin):
    list_display = ['swiperImgs']

    def delete_queryset(self, request, queryset):
        for obj in queryset:
            os.remove(obj.swiperImgs.path)
        super().delete_queryset(request, queryset)


admin.site.register(LogoBackgroundImgs, LogoBackgroundImgsAdmin)
admin.site.register(PersonalInfo)
admin.site.register(CV, CVAdmin)
admin.site.register(SwiperStack, SwiperStackAdmin)
admin.site.register(Groups)
admin.site.register(CareerInfo)
admin.site.register(Contact)
admin.site.register(FooterIcons)