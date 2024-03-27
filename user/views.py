from random import randint
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash, get_user_model
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from config.settings import sended_mails
from .forms import CustomUserForm


def register_view(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            form = CustomUserForm()
            return redirect('index')
    else:
        form = CustomUserForm()
        return render(request, 'registration/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            return redirect('index')
        else:
            form = PasswordChangeForm(request.user)
            return render(request, 'registration/change_password.html', {'form': form})
    else:
        form = PasswordChangeForm(request.user)
        return render(request, 'registration/change_password.html', {'form': form})


def confirm_email(request):
    if request.method == 'POST':
        try:
            recipient_list = [request.POST.get('email')]
            sended_mails[request.POST.get('email')] = f"{randint(100, 999)}-{randint(100, 999)}"

            send_mail(
                subject="Confirm email",
                message=sended_mails[request.POST.get('email')],
                from_email='info@sarvarazim.com',
                recipient_list=recipient_list
            )
            print(sended_mails)
            return redirect('confirm_email_confirm')
        except Exception as e:
            print(e)
            # return render(request, 'check_email/fail_send_email.html')
    return render(request, 'check_email/confirm_email.html')


def confirm_email_confirm(request):
    if request.method == 'POST':
        if sended_mails[request.user.email] == f"{request.POST.get('num1')}-{request.POST.get('num2')}":
            return redirect('index')
        else:
            return render(request, 'check_email/confirm_send_email.html')
    else:
        return render(request, 'check_email/confirm_send_email.html')


def check_email(request):
    if request.method == 'POST':
        user = get_user_model().objects.get(pk=request.user.pk)
        if user.is_email_verified:
            return True
        else:
            return False
