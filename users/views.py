from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    users = User.objects.all()
    params={'users':users}
    return render(request,'users/index.html',params)

def loginpage(request):
    return render(request,'users/login.html')

def signuppage(request):
    return render(request,'users/signup.html')



def handleLogin(request):
    if request.method == 'POST':
        # Getting POST data
        username = request.POST['user_name']
        password = request.POST['user_password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return redirect('/signup_page')
    else:
        return redirect('index')


def handleLogout(request):
    logout(request)
    return redirect('index')

def handleSignup(request):
    if request.method == 'POST':
        # Getting POST data
        username = request.POST['user_name']
        email = request.POST['user_email']
        pass_1 = request.POST['user_password_1']
        pass_2 = request.POST['user_password_2']

        # if pass_1 != pass_2:
        #     messages.error(request, "Passwords don't match")
        #     return redirect('/')

        myuser = User.objects.create_user(username, email, pass_1)
        myuser.save()
        user = authenticate(username=username, password=pass_1)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return redirect('/signup_page')
    else:
        return redirect('index')


def delete(request,pk):
    userDelete = User.objects.get(id=pk)
    userDelete.delete()
    return redirect('/logout')
    