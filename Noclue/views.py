from django.shortcuts import render 
from django.http import HttpResponseRedirect
from .forms import LogInForm
from .models import LogIn
from django.views import View
from django.contrib.auth import login
from django.views.generic import TemplateView


class LogInFormView(View):
    def get(self, request):
        form = LogInForm()
        return render(request, 'Noclue/index.html', {
            'form': form
        })

    def post(self, request):
        form = LogInForm(request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/test')

        return render(request, 'Noclue/index.html', {
            'form': form
        })


class ThankYouView(TemplateView):
    template_name = 'Noclue/test.html'
    

class UserInfoView(TemplateView):
    template_name = 'Noclue/Users.html'
    
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            user = LogIn.objects.all()
            context['user'] = user
            return context
        
        