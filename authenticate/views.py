from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib import messages
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login, logout


# Registration view
def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user =form.save()
            user.save()

              # Specify the authentication backend when logging in
            backend = 'django.contrib.auth.backends.ModelBackend'  # custom backend
            login(request, user, backend=backend)
            return redirect('register')

        else:
            messages.error(request, 'invalid information, please enter your info again')

        context= {'form':form}
        return render(request, 'authenticate/register.html', context)
    
# login view
def login_user(request):
    if request.method =='POST':
        form = LoginForm(request, data = request.POST)

        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password= password)
        if user is not None:
            login(request, user)
            return redirect('register')
        else:
            messages.error(request, 'Invalid username/email or password.')
        
        form = LoginForm(request.POST)
        context = {'form': form}
        return render(request, 'authenticate/login.html', context)
    

# view to logout users
def logout_user(request):
    if request.method == 'POST':
        logout(request)
    
    messages.info(request, 'You have successfully logged out.')
    return redirect('home')
