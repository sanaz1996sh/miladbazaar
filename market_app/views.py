from django.shortcuts import render,HttpResponse
from .models import *


# Create your views here.


def show(request,code):
    l2=shopcls.objects.filter(id=code)
    return render(request,"market_app/show-details.html",context={"d":l2})




def home(request):
   l=homeimgcls.objects.filter()
   return render(request,"market_app/index.html",context={"image":l})

def shop(request):
   l1=shopcls.objects.filter(phase=1)
   l2=shopcls.objects.filter(phase=2)
   
   return render(request,"market_app/shop.html",context={"shop1":l1,"shop2":l2, "active_tab":"shop"})

def blog(request):
    l1=blogcls.objects.all()
    l2=officecls.objects.all()
    return render(request,"market_app/blog.html",context={"blog1":l1,"office":l2,"active_tab":"blog"})

def contact(request):
    n=request.POST.get("name")
    e=request.POST.get("email")
    s=request.POST.get("subject")
    m=request.POST.get("message")
    if(n and e and s and m):
        contactcls.objects.create(name=n,email=e,subject=s,message=m)
        return render(request,"market_app/message.html",{"active_tab":"contact"})
    return render(request,"market_app/contact.html",{"active_tab":"contact"})

def services(request):
    l=servicescls.objects.all()
    return render(request,"market_app/services.html",context={"serv":l, "active_tab":"services"})

def about(request):
    l=aboutcls.objects.all()
    return render(request,"market_app/about.html",context={"about1":l ,"active_tab":"about"})