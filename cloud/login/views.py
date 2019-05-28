from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Login
from django.db import IntegrityError
# Create your views here.

current_user=""

def user_login(request):
    return render(request,'login.html')

def auth_user(request):
    u = request.POST['uname']
    p = request.POST['pass']
    request.session["current_user"]=u
    print(u,p)
    users= Login.objects.raw("SELECT * FROM login_login where username=%s",[u])
    current_user=users[0].username
    print("cu:",current_user)
    try:    
        if(users[0].password==p):
            return redirect('/feedpage/')
            #return render(request,'feedpage.html')
            #return HttpResponse("<h1>Welcome to Cloud</h1><a href=\"/ \">Logout</a>")
        else:
            return HttpResponse("<h1>Try Again</h1><br><br><a href=\"/ \">Redirect to Login</a>")
    except IndexError:
        return HttpResponse("<h1>Username Doesnot Exist</h1><a href=\"/create \">Create Account</a>")
    # Below is the alternate method to get values as a list of tupes from the database
    # But I like the above method as we have the freedom to use sql.
    #users=Login.objects.all().values_list()
def add_user(request):
    return render(request,'create.html')

def create_user(request):
    u = request.POST['u_username']
    p = request.POST['u_password']
    if u=="" or p=="":
        return HttpResponse("<h1>Invalid Password</h1>")
    else:
        user_detail = Login(username=u,password=p)
        try:
            user_detail.save()
        except IntegrityError:
            return HttpResponse("<h1>Username Aldready exists</h1>")
        return redirect('/')
