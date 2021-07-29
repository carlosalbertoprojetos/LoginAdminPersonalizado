from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView

from .models import Profile, User
from .forms import RegisterForm, ProfileForm


# def home(request):
#     return render(request, 'home.html')


# def register_View(request):
#     form = User()
#     return render(request, 'usuario/signup.html', {'form':form})


from django.urls import reverse_lazy


class RegisterView(SuccessMessageMixin, CreateView):
    # model = User
    template_name = 'usuario/signup.html'
    form_class = RegisterForm
    success_message = 'Cadastrado com sucesso!'
    success_url = '/'

    def form_valid(self, form): 
        obj = form.save(commit=False)
        obj.save()
        return super().form_valid(form)
    
class ProfileView(LoginRequiredMixin, CreateView):
    form_class = ProfileForm
    template_name = 'usuario/signup2.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.email = self.request.user
        obj.active = False
        obj.save()
        return super().form_valid(form)


class DashboardView(TemplateView):
    model = Profile
    template_name = 'usuario/dashboard.html'
