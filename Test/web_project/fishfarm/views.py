from django.shortcuts import render
from django.http import HttpResponseRedirect
from . models import *
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from django.shortcuts import redirect, render
from django.contrib.auth  import authenticate,  login, logout
from django.contrib import messages 
from django.contrib.auth.models import User 
import smtplib, ssl
from email.mime.text import MIMEText
# Create your views here.
def home(request):
    p =products.objects.all()
    sp=sproducts.objects.all()
    tm=team.objects.all()
    return render(request, 'index.html',{'product':p, 'sproduct':sp,'team': tm})
def contact(request):
    if request.method == "POST":  
       Name= request.POST['NAME']
       Email= request.POST['EMAIL']
       Subject = request.POST['SUBJECT']
       Message = request.POST['MESSAGE']
       ins=contact(name=Name,email=Email,subject=Subject,message=Message)
       ins.save()
    return render(request, 'contact.html')
def register(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['Username']
        email=request.POST['Email']
        fname=request.POST['Fname']
        lname=request.POST['Lname']
        pass1=request.POST['Password']
        pass2=request.POST['Confirm Password']

        # check for errorneous input
        if (pass1!= pass2):
            messages.error(request, " Passwords do not match")
            return redirect('register')
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, " Your Fish Farm account has been successfully created")
        return redirect('login')
    return render(request, 'register.html')

        
def signin(request):
    if request.method=="POST":
        # Get the post parameters

        loginusername=request.POST['Username']
        loginpassword=request.POST['password']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            
            messages.success(request, "Successfully Logged In")
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("login")
    return render(request, 'login.html')

def band_listing(request):
    logins = models.login.objects.all()
    return render(request, 'login/login.html', {'logins': logins})
def myaccount(request):
    return render(request, 'myAccount.html')
def about(request):
    return render(request, 'about.html')
def ourteam(request):
    tm=team.objects.all()
    return render(request, 'our-team.html',{'team': tm})

def Logouts(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')

@login_required(login_url="/users/login")
def cart_add(request, id):
    cart = Cart(request)
    product = products.objects.get(id=id)
    cart.add(product=product)
    return redirect("home")


@login_required(login_url="/users/login")
def item_clear(request, id):
    cart = Cart(request)
    product = products.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_increment(request, id):
    cart = Cart(request)
    product = products.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = products.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart_detail(request):
    return render(request, 'cart.html')
def store(request):
    cart = Cart(request)
    ab=request.session['cart']
    print(ab)
    req.objects.create()
    max_val=req.objects.latest('id')
    print(max_val)
    for key,value in ab.items():
        print(value['name'])

        orderel.objects.create(order=max_val, name=value['name'], quan=value['quantity'], price=value['price'])
        form1 = User.objects.get(username=request.user)
        email= form1.email
        sender = 'sohaibjutt6162@gmail.com'
        receivers = [email]
        body_of_email = 'thanks for shoping.'
        msg = MIMEText(body_of_email, 'html')
        msg['Subject'] = 'Oder success'
        msg['From'] = sender
        msg['To'] = ','.join(receivers)
        s = smtplib.SMTP_SSL(host = 'smtp.gmail.com', port = 465)
        s.login(user = 'sohaibjutt6162@gmail.com', password = 'sohaib5512')
        s.sendmail(sender, receivers, msg.as_string())
        s.quit()
        print("Email has been sent sucessfully!")

    cart.clear()

    return render(request, 'index.html', {'cart': cart})