from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .forms import SignUpForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
# Create your views here.

def login(request):
    return render(request, 'registration/login.html')


class UserRegisterView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('account:login')
    
@login_required(login_url='account:login')
def Profile(request):
    return render(request, 'registration/profile.html')