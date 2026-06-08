from django.shortcuts import render
from django.shortcuts import redirect

from .forms import RegisterForm

from django.contrib.auth import authenticate
from django.contrib.auth import login

from django.contrib.auth import logout


def register(request):

    form = RegisterForm(
        request.POST or None
    )

    if form.is_valid():
        form.save()
        return redirect(
            'login'
        )
    return render(
        request,
        'accounts/register.html',
        {
            'form': form,
        }
    )

def user_login(request):

    if request.method == 'POST':
        username = request.POST[
            'username'
        ]
        password = request.POST[
            'password'
        ]
        
        user = authenticate(
            username=username,
            password=password
        )

        if user:

            login(
                request,
                user
            )

            return redirect(
                'student_list'
            )
    return render(
        request,
        'accounts/login.html'
    )

def user_logout(request):

    logout(request)

    return redirect(
        'login'
    )
# Create your views here.
