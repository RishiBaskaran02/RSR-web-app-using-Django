import email, os
from itertools import product
from tokenize import String
from django.shortcuts import redirect, render
from django.http import HttpResponse,Http404,HttpResponseRedirect, FileResponse
from django import template
from django.template import loader 
from cgitb import html
from django.core.mail import send_mail
from APP.models import signin
from APP.models import Product
from APP.models import OfficeSignin
from APP.models import Adminsignin,Verification
from django.core.files.base import ContentFile
# Create your views here.


def Homepage(request):
      return render (request,'RSRhomepage.html')



#Register
def register(request):
      if request.method == "POST":
             fullname = request.POST['fullname']
             email = request.POST['email']
             DOB = request.POST['dob']
             Phone = request.POST['phone']
             password = request.POST['password']
             ins = signin(fullname=fullname,email=email,DOB=DOB,Phone=Phone,password=password)
             ins.save()
             return render(request,"RSRhomepage.html")
      return render (request,'Register.html',)

#Login
def Login(request):
      error = False
      if request.method == "POST":
            email = request.POST.get('email')
            password = request.POST.get('password')
            if email == "admin@gmail.com" and password == "adminrishi":
                  return HttpResponseRedirect('/Adminhome/')
            elif email == "office@gmail.com" and password == "officerishi":
                  return HttpResponseRedirect('/Oficehome/')
            for each in signin.objects.all():
                  if email == each.email and password == each.password:
                        CurrentUser = signin.objects.filter(email = email)
                        request.session['username'] = CurrentUser[0].fullname
                        request.session.modified = True
                        return HttpResponseRedirect('/Homepage/')
                  else:
                        error = True
                  

      return render(request, 'login.html',{'error':error})

#Logout
def Logout(request):
      try:
            del request.session['username']
      except: pass
      request.session.modified = True
      return HttpResponseRedirect('/Homepage/')
def Products(request):
      return render (request,'Products.html')

def About(request):
      return render (request,'About.html')

def Contact(request):
      return render (request,'Contact.html')



def Alogin(request):
      return render (request,'Alogin.html')

def Verificationn(request):
      if request.method == "POST":
            fullname = request.POST.get('fullname')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            farmAddress = request.POST.get('farmAddress')
            farmRegNo = request.POST.get('farmRegNo')
            certificate = request.FILES.get('farmCertificate')
            print(fullname, email, phone, farmAddress, farmRegNo, certificate)
            ins = Verification(fullname= fullname, email= email,phone= phone,farmAddress= farmAddress,farmRegNo= farmRegNo, certificate= certificate)
            ins.save()
            return HttpResponseRedirect('/Account/')
      return render(request, 'verification.html')

def Account(request):
      return render(request,'Account.html')
def Profileedit(request):
      return render(request,'Profileedit.html')



def Forgot(request):
          print("the method is",request.method)
          if(request.method == "POST"):
                email=request.POST['email']
                npassword=request.POST['npassword']
                signin.objects.filter(email=email).update(password=npassword)
                print("Data updated successfully!")
          else:
                print("redirected")
          return render(request,'Forgot.html')


def Adminhome(request):
      return render (request,'Adminhome.html')



def OfficeLogin(request):
      error = False
      if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            for each in OfficeSignin.objects.all():
                  if username == each.username and password == each.password:
                        return HttpResponseRedirect('/Adminhome/')
                  else:
                        error = True

      return render(request, 'AdminLogin.html',{'error':error})






def PassCheck(request):
      OldPass = request.GET['Oldpass']
      CurrentUser = request.session.get('username')
      record = signin.objects.filter(fullname= CurrentUser)
      if record[0].password == OldPass:
            return HttpResponse(1)
      else:
            return HttpResponse(0)

def UpdateAccount(request):
      if request.method == "POST":
            print("asds")
            CurrentUser = request.session.get('username')
            dob = request.POST.get('dob')
            phone = request.POST.get('phone')
            address = request.POST.get('address')
            Npassword = request.POST.get('Npassword')
            signin.objects.filter(fullname= CurrentUser).update(DOB= dob,Phone= phone,password= Npassword,address= address)
            return HttpResponseRedirect('/Profileedit')
      return render(request, 'profileedit.html')

def adminVerification(request):

            return render(request, 'adminVerification.html',{
                  'VerficationData' : Verification.objects.all()
            })

def openFile(request):
      record = Verification.objects.filter(farmRegNo= request.POST['farmRegNo'])
      filepath = os.path.join('', str(record.first().certificate))
      return FileResponse(open(filepath, 'rb'), content_type='application/pdf')

def makeVerify(request):
      Verification.objects.filter(farmRegNo= request.GET['farmRegNo']).update(verified=1)
      return HttpResponse("Verified")



def productsadmin(request):
      if request.method == "POST":
            pname = request.POST.get('pname')
            pquantity = request.POST.get('pquantity')
           
            print(pname,pquantity)
            ins = Product(pname=pname, pquantity=pquantity)
            ins.save()
            return HttpResponseRedirect('/padmin')
      return render(request, 'productsadmin.html')

def productsadmin2(request):
      if request.method == "POST":
            pname = request.POST.get('pname')
            npquantity = request.POST.get('npquantity')
           
            
            Product.objects.filter(pname=pname).update(pquantity=npquantity)
            return HttpResponseRedirect('/padmin2')
      return render(request, 'productsadmin2.html')

def office(request):
    shows = []
    shows = Product.objects.all()
    for show in shows:
        print(show.pname,show.pquantity)
    return render(request, 'officechecks.html', {'shows': shows})
      
def adminLogout(request):
      return HttpResponseRedirect('/Homepage/')

def Officehome(request):
      return render(request, 'Officehome.html')
