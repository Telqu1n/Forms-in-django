from django.shortcuts import render 
from django.http import HttpResponseRedirect
from .forms import LogInForm
from .models import LogIn


def index(request):
   if request.method == 'POST':
       form = LogInForm(request.POST)
       
       if form.is_valid():
           user_data = LogIn(username=form.cleaned_data['username'], 
                             password=form.cleaned_data['password'], 
                             email=form.cleaned_data['email'])
           user_data.save()
           return HttpResponseRedirect('/test')
   else:
       form = LogInForm()
        
   return render(request, 'Noclue/index.html',{
         'form': form})
   
   
def about(request):
    return render(request, 'Noclue/test.html')  