from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.urls import reverse_lazy

from helperfuns.findregionfromip import findregionfromip
from helperfuns.sendmail import sendmail

from portfolioapp1.models import Contact

class IndexView(View):
    template = "portfolioapp1/index.html"
    success_url = reverse_lazy("portfolioapp1:Index")

    def get(self, request):

        # location of visitor to your page
        # print('REQUESTS: ', request.headers)
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
    
        return render(request, self.template)
    
    def post(self, request):
        post_data = request.POST
        fn = post_data.get('firstname')
        email = post_data.get('emailaddress')
        msg = post_data.get('message')
        contact = Contact(name=fn,email=email,message=msg)
        contact.save()

        # sendmail(recipient=email)     # Mail to visitor
        sendmail(subject="New Message from "+fn+" ["+email+"]", message=msg) # Mail to Me(developer)

        return redirect(self.success_url)