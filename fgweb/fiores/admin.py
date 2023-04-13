from django.contrib import admin
import os
from image_cropping import ImageCroppingMixin
from adminsortable2.admin import SortableAdminMixin

from fiores.models import SliderImgs, Contact, Members, Projects

# Register your models here.

class SliderImgsAdmin(ImageCroppingMixin, admin.ModelAdmin):
    def delete_queryset(self, request, queryset):
        for obj in queryset:
            os.remove(obj.sliderImg.path)
        super().delete_queryset(request, queryset)

class ContactAdmin(admin.ModelAdmin):
    def delete_queryset(self, request, queryset):
        for obj in queryset:
            os.remove(obj.cv.path)
        super().delete_queryset(request, queryset)

class MembersAdmin(SortableAdminMixin, ImageCroppingMixin, admin.ModelAdmin):
    list_display = ['name', 'my_order']
    ordering = ['my_order']
    def delete_queryset(self, request, queryset):
        for obj in queryset:
            os.remove(obj.photo.path)
        super().delete_queryset(request, queryset)

class ProjectsAdmin(ImageCroppingMixin, admin.ModelAdmin):
    def delete_queryset(self, request, queryset):
        for obj in queryset:
            os.remove(obj.logo.path)
            os.remove(obj.image1.path)
            os.remove(obj.image2.path)
        super().delete_queryset(request, queryset)

admin.site.register(SliderImgs, SliderImgsAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Members, MembersAdmin)
admin.site.register(Projects, ProjectsAdmin)