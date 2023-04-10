from django.contrib import admin
import os

from fiores.models import SliderImgs, Contact, Members, Projects

# Register your models here.

class SliderImgsAdmin(admin.ModelAdmin):
    def delete_queryset(self, request, queryset):
        for obj in queryset:
            os.remove(obj.sliderImg.path)
        super().delete_queryset(request, queryset)

class ContactAdmin(admin.ModelAdmin):
    def delete_queryset(self, request, queryset):
        # Delete the associated file for each object in the queryset selected from the Action dropdown in admin
        # https://docs.djangoproject.com/en/4.2/ref/contrib/admin/actions/
        for obj in queryset:
            os.remove(obj.cv.path)
        # Call the parent method to delete the queryset from the database
        super().delete_queryset(request, queryset)

class MembersAdmin(admin.ModelAdmin):
    def delete_queryset(self, request, queryset):
        for obj in queryset:
            os.remove(obj.photo.path)
        super().delete_queryset(request, queryset)

class ProjectsAdmin(admin.ModelAdmin):
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