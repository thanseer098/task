from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import Registerform,Loginform,UpdateForm,changepasswordform
from .models import Gallary, Register
from django.contrib.auth import logout as logouts
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def index(request):
    return render (request,'index.html')
def registration(request):
    if request.method == 'POST':
        form=Registerform(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            age=form.cleaned_data['age']
            place=form.cleaned_data['place']
            photo=form.cleaned_data['photo']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            confirmpassword=form.cleaned_data['ConfirmPassword']

            user=Register.objects.filter(email=email).exists()
            if user:
                messages.warning(request,'Email Alredy exist')
                return redirect('/login')
            elif password!=confirmpassword:
                messages.warning(request,'Password Mismatch')
            else:
                tab=Register(name=name,age=age,place=place,email=email,photo=photo,password=password)
                tab.save()
                subject='welcome to web page'
                message=f'hai {name},thanks for registering'
                email_from = settings.EMAIL_HOST_USER  
                recipient_list = [email,]
                send_mail(subject, message, email_from, recipient_list)
                messages.success(request,'DATA SAVED')
                return redirect('/login')
    else:
        form=Registerform() 
    return render(request,'registration.html',{'form':form})
def login(request):
    if request.method == 'POST':
        form=Loginform(request.POST)
        if form.is_valid():
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            try:
                user=Register.objects.get(email=email)
                if not user:
                    messages.warning(request,'Email does not exist')
                    return redirect('/login')
                elif password!=user.password:
                    messages.warning(request,'password Incorrect')
                    return redirect('/login')
                else:
                    messages.success(request,'Success')
                    return redirect('/home/%s' % user.id)
            except:
                messages.warning(request,'email or password incorrect')
                return redirect('/login')
    else:
        form=Loginform()
    return render(request,'login.html',{'form':form})
def home(request,id):
        user=Register.objects.get(id=id)
        return render(request,'home.html',{'user':user})

def update(request,id):
    user=Register.objects.get(id=id)
    if request.method=='POST':
        form=UpdateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Success')
            return redirect('/home/%s' % user.id)
    else:
        form=UpdateForm(instance=user)
    return render(request,'update.html',{'user':user,'form':form})
def delete(request,id):
    user=Register.objects.get(id=id)
    user.delete()
    messages.success(request,'SUCCESS')
    return redirect('/')
def logout(request,id):
    logouts(request)
    messages.success(request,'SUCCESS')
    return redirect('/')
def changepassword(request,id):
    user=Register.objects.get(id=id)
    if request.method == 'POST':
        form=changepasswordform(request.POST)
        if form.is_valid():
            oldpassword=form.cleaned_data['oldpassword']
            newpassword=form.cleaned_data['newpassword']
            confirmpassword=form.cleaned_data['confirmpassword']
            if oldpassword!=user.password:
                messages.warning(request,'incorrect')   
                return redirect('/changepassword/%s'% user.id )
            elif oldpassword==newpassword:
                messages.warning(request,'password similar')
                return redirect('/changepassword/%s' % user.id)
            elif newpassword!=confirmpassword:
                messages.warning(request,'password new')
                return redirect('/changepassword/%s' % user.id)
            else:
                user.password=newpassword
                user.save()
                messages.success(request,'change success')
    else:
        form=changepasswordform()
    return render(request,'changepassword.html',{'user':user,'form':form})
def logout(request):
    logouts(request)
    messages.success(request,"logged out")
    return redirect('/')
def gallary(request):
    images=Gallary.objects.all()
    return render (request,'gallary.html',{'images':images})

    




        
