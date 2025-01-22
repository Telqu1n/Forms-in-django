from django.shortcuts import render, get_object_or_404 
from django.http import HttpResponseRedirect, Http404
from .forms import LogInForm
from .models import LogIn
from django.views import View
from django.contrib.auth import login
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView

#This is the view for the login form using the FormView
# class LogInFormView(FormView):
#    form_class = LogInForm
#    template_name = 'Noclue/index.html'
#    success_url = '/test'

#    def form_valid(self, form):
#        form.save()
#        return super().form_valid(form)



#This is a view for the login form using the CreateView
class LogInFormView(CreateView):
    model = LogIn
    form_class = LogInForm
    template_name = 'Noclue/index.html'
    success_url = '/test'


class ThankYouView(TemplateView):
    template_name = 'Noclue/test.html'
    
    

class UserInfoView(ListView):
    template_name = 'Noclue/Users.html'
    
    model = LogIn
    context_object_name = 'user'



class UserDetailView(DetailView):
    template_name = 'Noclue/user_info.html'
    model = LogIn
    
    context_object_name = 'user_details'
    
    