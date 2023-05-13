from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.urls import reverse_lazy

from CompanyApp.models import MemberInfo, SliderImgs, Story, HomeColumn2, About, Project, Groups, Contact, FooterText, FooterIcon

# Create your views here.

class IndexView(View):
    template = "CompanyApp/index.html"

    def get(self, request):
        # member = MemberInfo.objects.all()[0].picture
        sliderImgs = SliderImgs.objects.all()
        count = len(list(SliderImgs.objects.all()))
        count = list(range(count))
        story = ""
        if len(Story.objects.all()) > 0 :
            story = Story.objects.last().text.split(" ")[:8]
            story = " ".join(story)+"...."
        homeColumn2 = HomeColumn2.objects.last()
        footerText = FooterText.objects.last()
        footerIcon = FooterIcon.objects.all()
       
        ctx = {"sliderImgs":sliderImgs, "count":count, 
        "story":story, "homeColumn2": homeColumn2, 
        "footerText": footerText, "footerIcon":footerIcon}

        return render(request, self.template, ctx)

class AboutView(View):
    template = "CompanyApp/about.html"

    def get(self, request):
        about = About.objects.all()
        footerText = FooterText.objects.last()
        footerIcon = FooterIcon.objects.all()
        ctx = {"about": about, 
        "footerText": footerText, "footerIcon":footerIcon}
        return render(request, self.template, ctx)

class ProjectsView(View):
    template = "CompanyApp/projects.html"

    def get(self, request):
        projects = Project.objects.all()
        footerText = FooterText.objects.last()
        footerIcon = FooterIcon.objects.all()
        ctx = {"projects": projects, 
        "footerText": footerText, "footerIcon":footerIcon}
        return render(request, self.template, ctx)

class TeamView(View):
    template = "CompanyApp/team.html"

    def get(self, request):
        # member = MemberInfo.objects.all()[0].picture
        groups = Groups.objects.all()
        members = MemberInfo.objects.all()
        footerText = FooterText.objects.last()
        footerIcon = FooterIcon.objects.all()
        ctx = {"groups":groups, "members":members, 
        "footerText": footerText, "footerIcon":footerIcon}
        return render(request, self.template, ctx)

class StoryView(View):
    template = "CompanyApp/story.html"

    def get(self, request):
        story = Story.objects.last()
        footerText = FooterText.objects.last()
        footerIcon = FooterIcon.objects.all()
        ctx = {"story":story, 
        "footerText": footerText, "footerIcon":footerIcon}
        return render(request, self.template, ctx)

class ContactView(View):
    template = "CompanyApp/contact.html"
    success_url = reverse_lazy("CompanyApp:confirmation")

    def get(self, request):
        footerText = FooterText.objects.last()
        footerIcon = FooterIcon.objects.all()
        ctx = {"footerText": footerText, "footerIcon":footerIcon}
        return render(request, self.template, ctx)
    
    def post(self, request):
        post_data = request.POST
        fn = post_data.get('fullname')
        email = post_data.get('emailaddress')
        msg = post_data.get('message')
        contact = Contact(name=fn,email=email,message=msg)
        contact.save()

        return redirect(self.success_url)

class ConfirmationView(View):
    template = "CompanyApp/confirm.html"

    def get(self, request):
        return render(request, self.template)