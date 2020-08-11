from django.http import HttpResponse
from django.shortcuts import render
from .forms import CityForm
from django.shortcuts import redirect
from django.views.decorators.http import require_POST
from .models import user,challan,p_user,diversion, enquiry,news
from django.contrib import messages

from rest_framework import generics

def diversion_delete(request, d_id):
    diversion.objects.filter(pk=d_id).delete()
    return redirect("d_diversion")

def d_diversion(request):
    all_d = diversion.objects.order_by("-date")
    all_n = news.objects.order_by("-date");
    nd = all_n[:4]
    context = {'all_d':all_d,'nd':nd}
    return render(request,"d_diversion.html",context)

def diversion_page(request):
    return render(request,"diversion.html")

def homepage(request):
    return render (request,"index2.html")


def login(request):
     return render (request,"login.html")

def login_1(request):
    user_1= request.POST.get('username')
    pass_1= request.POST.get('pass')
    a_user= user.objects.filter(u_name=user_1,password = pass_1).first()
    context= {'a_user':a_user}
    if(a_user.active == True):
        return render (request,"profile3.html", context)
    else:
        return render ( request,"login.html")
def p_login(request):
    user_1 = request.POST.get('username')
    pass_1 = request.POST.get('pass')
    a_user = p_user.objects.filter(pu_name=user_1,password=pass_1).first()
    all_n = news.objects.order_by("-date");
    nd = all_n[:4]
    context = {'a_user':a_user,'nd':nd}
    print(a_user)
    if(a_user):
        return render(request,"profile2.html",context)
    else:
        return render( request,"login.html")

def register(request):
    all_n = news.objects.order_by("-date");
    nd = all_n[:4]
    context={'nd':nd}
    return render (request,"register.html",context)

def new_user(request):
    user_1 = request.POST.get('username')
    first =request.POST.get('first')
    last = request.POST.get('last')
    key = request.POST.get('key')
    email = request.POST.get('e_m')
    licence = request.POST.get('licence')
    todo = user.objects.filter(licence_no = licence)
    all_n = news.objects.order_by("-date");
    nd = all_n[:4]
    if(todo):
        messages.info(request,'user already exist')
        return redirect('register')
    if(user.objects.filter(u_name=user_1).exists()):
        messages.info(request,'username already exist')
        return redirect('register')
    new = user(u_name=user_1,f_name=first,l_name=last,password=key,licence_no=licence,e_mail=email,active = True)
    new.save()
    a_user = user.objects.get(licence_no = licence)
    context={'a_user':a_user,'nd':nd}
    return render(request,"profile3.html", context)
    

def profile(request):
    return render (request,"profile.html")

def report(request):
    return render (request,"report.html")

def contact(request):
    all_n = news.objects.order_by("-date");
    nd = all_n[:4]
    context = {'nd':nd}
    return render (request,"contact.html",context)

def contact_form(request):
    email = request.POST.get('email')
    name = request.POST.get('name1')
    comment = request.POST.get('comment')
    subject = request.POST.get('head')
    enquiry.objects.create(e_mail=email,u_name = name, issue = comment)
    return render(request, "contact.html")

def error(request):
    return render(request,"404.html")

def a_challan(request):
    return render(request,"challan.html")

def i_challan(request):
    licence=request.POST.get('license')
    inst=request.POST.get('comment')
    amount = request.POST.get('amount')
    challan.objects.create(license_no = licence, comment = inst,amount = amount)
    messages.info(request, ' Challan Issued Successfully')
    return redirect ('a_challan')

def view_challan(request,licence_no):
    all_c = challan.objects.filter(license_no=licence_no)
    all_n = news.objects.order_by("-date");
    nd = all_n[:4]
    context = {'all_c':all_c,'nd':nd}
    return render(request,"v_challan.html",context)

def view_user(request):
    licence = request.POST['licence']
    user_1 = user.objects.get(licence_no = licence)
    context = {'user_1':user_1}
    

def report_1(request):
    user_1 = request.POST.get('license')
    user.objects.filter(licence_no=user_1).update(active = False)
    messages.info(request, ' User Reported')
    return redirect('report')

def add_diversion(request):
    origin = request.POST['start']
    destination = request.POST['dest']
    route = request.POST['route']
    diversion.objects.create(start = origin, dest = destination, diver = route)
    messages.info(request, ' Diversion Added')
    return redirect('diversion_page')

def view_diversion(request):
    all_d = diversion.objects.order_by("date")
    all_n = news.objects.order_by("-date");
    nd = all_n[:4]
    context = {'all_d':all_d,'nd':nd}
    return render(request,"v_diversion.html",context)

def news1(request):
    all_n = news.objects.order_by("-date");
    nd = all_n[:4]
    context = {'nd':nd}
    return render(request,"news.html",context)



def view_news(request):
    news1 = news.objects.order_by("-date")
    all_n = news.objects.order_by("-date");
    nd = all_n[:4]
    context = {'news1':news1,'nd':nd}
    return render(request,"v_news.html",context)

def add_news(request):
    head = request.POST.get('head_news')
    comment = request.POST.get('body_news')
    news.objects.create(heading = head, content = comment)
    messages.info(request, ' News Added Successfully')
    return redirect('news1')

def about(request):
    return render(request,"about.html")

def gallery(request):
    dests = media.objects.all()
    return render(request,'gallery.html', {'dests':dests})

def article(request):
  #  news1 = news.objects.get(pk=news_id)
   # all_n = news.objects.order_by("-date");
    #nd = all_n[:4]
    #ontext = {'news1':news1,'nd':nd}

    return render(request,"article.html")

def article_details(request):
    news_1=news.objects.filter(pk=news_id)
    return render(request,"article_details.html")




    
    
    
    
    
    
    

