from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.urls import reverse_lazy

from fiores.models import SliderImgs, Contact, Members, Projects

# Create your views here.

class IndexView(View):
    template = "fiores/index.html"
    success_url = reverse_lazy("fiores:index")

    def get(self, request):
        slider = SliderImgs.objects.all()

        ctx = {'slider':slider}

        return render(request, self.template, ctx)
    
    def post(self, request):
        post_data = request.POST
        name = post_data.get('contact-us-name')
        sub = post_data.get('contact-us-subject')
        email = post_data.get('contact-us-email')
        msg = post_data.get('contact-us-message')
        cv = request.FILES['cv']
        print(cv)

        contact = Contact(name=name,email=email, subject=sub ,message=msg, cv=cv)
        contact.save()

        return redirect(self.success_url)

class AboutView(View):
    template = "fiores/about.html"

    def get(self, request):
        return render(request, self.template)

class TeamView(View):
    template = "fiores/team.html"

    def get(self, request):
        members = Members.objects.all()

        ctx = {'members':members}

        return render(request, self.template, ctx)

class ProjectsView(View):
    template = "fiores/projects.html"

    def get(self, request):
        projects = Projects.objects.all()
        
        ctx = {'projects':projects}
        return render(request, self.template, ctx)