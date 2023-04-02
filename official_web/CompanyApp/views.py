from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.urls import reverse_lazy

from CompanyApp.models import MemberInfo, SliderImgs

# Create your views here.

class IndexView(View):
    template = "CompanyApp/index.html"

    def get(self, request):
        # member = MemberInfo.objects.all()[0].picture
        sliderImgs = SliderImgs.objects.all()
        count = len(list(SliderImgs.objects.all()))
        count = list(range(count))
        ctx = {"sliderImgs":sliderImgs, "count":count}
        return render(request, self.template, ctx)

class AboutView(View):
    template = "CompanyApp/about.html"

    def get(self, request):
        return render(request, self.template)

class ProjectsView(View):
    template = "CompanyApp/projects.html"

    def get(self, request):
        return render(request, self.template)

class TeamView(View):
    template = "CompanyApp/team.html"

    def get(self, request):
        # member = MemberInfo.objects.all()[0].picture
        membersGlobal = MemberInfo.objects.filter(group='Global')
        membersRed = MemberInfo.objects.filter(group='Red')
        membersBlue = MemberInfo.objects.filter(group='Blue')
        membersGreen = MemberInfo.objects.filter(group='Green')
        ctx = {'membersGlobal':membersGlobal, 'membersRed':membersRed, 'membersBlue':membersBlue, 'membersGreen':membersGreen}
        return render(request, self.template, ctx)

class StoryView(View):
    template = "CompanyApp/story.html"

    def get(self, request):
        return render(request, self.template)