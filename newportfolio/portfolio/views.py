from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.urls import reverse_lazy

from helperfuns.findregionfromip import findregionfromip
from helperfuns.sendmail import sendmail

from portfolio.models import LogoBackgroundImgs, SwiperStack, FooterIcons, CV, PersonalInfo, Groups, CareerInfo, Contact

# from portfolio.models import

# Create your views here.

class IndexView(View):
    template = "portfolio/index.html"
    success_url = reverse_lazy("portfolio:index")

    def get(self, request):
        back = LogoBackgroundImgs.objects.last()
        PI = PersonalInfo.objects.last()
        cv = CV.objects.last()
        swiperstack = SwiperStack.objects.all()
        footer = FooterIcons.objects.all()
        groups = Groups.objects.all()
        careerInfo = CareerInfo.objects.all()

        # location of visitor to your page
        print('REQUESTS: ', request.headers)
        # visitor_ip=request.headers['X-Real-Ip'] #X-Real-Ip => Django 3.2.5
        visitor_ip= '39.43.87.38'
        visitor_location = findregionfromip(visitor_ip)
        req_headers = ""
        req_META = ""
        for key,val in request.headers.items():
            req_headers += key + ": " + val + "\n"
        for key, val in request.META.items():
            req_META += key + ": " + str(val) + "\n"
        sendmail(subject="New Visitor from "+visitor_location, message="You have a new visitor from "+visitor_location+" ["+visitor_ip+"]\n\n"+req_headers+"\n"+req_META)
    

        ctx = {'back': back, 'PI': PI, 'cv':cv, 'swiperstack':swiperstack, 'footer':footer, 'groups':groups, 'careerInfo': careerInfo}
        return render(request, self.template, ctx)
    
    def post(self, request):
        post_data = request.POST
        fn = post_data.get('fullname')
        email = post_data.get('emailaddress')
        msg = post_data.get('message')
        contact = Contact(name=fn,email=email,message=msg)
        contact.save()

        sendmail(recipient=email)     # Mail to visitor
        sendmail(subject="New Message from "+fn+" ["+email+"]", message=msg) # Mail to Me(developer)

        return redirect(self.success_url)