from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, DetailView

class LoginGate(View):
    model = User
    template_name = 'auth/login.html'

    def get(self, request):
        return render(request, self.template_name)
    
    def form_valid(self, form):
        return super(LoginGate, self).form_valid(form)
    
    def post(self, request):
        username, password = request.POST['username'], request.POST['password']
        user = authenticate(username=username, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        login(self.request, user)
        return HttpResponseRedirect(f'/user-profile/')

class RegistrationGate(TemplateView):
    template_name = 'auth/register.html'

class ProfileGate(TemplateView):
    template_name = 'users/profile.html'

class ProfileView(LoginRequiredMixin, TemplateView):
    model = User
    template_name = 'users/profile.html'

    # def get(self, request):
    #     current_user = request.user
    #     if current_user.is_authenticated:
    #         context = current_user
        

            
        # user = authenticate(username)
    
    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        return context

class RegisterUser(CreateView):
    model = User
    template_name = 'auth/register.html'
    fields = ['username', 'password']
    success_url = '/user-profile/'

    def form_valid(self, form):
        context = super(RegisterUser, self).form_valid(form)
        User.objects.create_user(username=context.username, password=context.password)
        messages.success(self.request, "User has registered.")
        return HttpResponseRedirect('/user-profile/')

class UpdateUser(UpdateView):
    model = User
    fields = ['__all__']
