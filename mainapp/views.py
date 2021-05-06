from django.http import HttpResponse
from django.shortcuts import render, redirect
import datetime
# Create your views here.
from .models import homepage,donate,contact

import razorpay
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string


def home(request):
    if request.method=='GET':
        obj1 = homepage.objects.get(id=1)
        obj2 = homepage.objects.get(id=2)
        obj3 = homepage.objects.get(id=3)
        obj4 = homepage.objects.get(id=4)
        obj5 = homepage.objects.get(id=5)

        return render(request,'home.html',{'obj':obj1,'obj1':obj2,'obj2':obj3,'obj3':obj4,'obj4':obj5})
    else:

        return redirect('payment')

def payment(request):
    name=request.POST.get('name')
    amount=int(request.POST.get('amount'))*100
    email=request.POST.get('email')
    client=razorpay.Client(auth=('rzp_test_iXfpXlITWNKm0U','wOFXoqlcxU5GLTSkQeVxes1q'))
    payment=client.order.create({'amount':amount,'currency':'INR','payment_capture':'1'})
    d=donate(name=name,amount=amount//100,email=email,payment_id=payment['id'])
    d.save()
    return render(request,'payment.html',{'name':name,'email':email,'amount':amount,'payment':payment})


def success(request):
    a=request.POST
    order_id=""
    for key,val in a.items():
        if key=='razorpay_order_id':
            order_id=val
            break
    user=donate.objects.filter(payment_id=order_id).first()
    user.paid=True
    user.save()
    now=datetime.datetime.now()
    msg_html=render_to_string('email.html',{'amount':user.amount,'name':user.name,'email':user.email,'payment_id':user.payment_id,'date':now.strftime('%d-%m-%y')})
    send_mail("Your donation has been received",'thank You',settings.EMAIL_HOST_USER,[user.email],html_message=msg_html)
    return render(request,'success.html')

def contactus(request):
    name=request.POST.get('contactname')
    email=request.POST.get('contactemail')
    message=request.POST.get('message')
    contact(name=name, email=email,message=message).save()
    print(name,email,message)
    return redirect('home')