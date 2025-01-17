from django.shortcuts import render 
from django.http import HttpResponseRedirect
from .forms import LogInForm


def index(request):
   if request.method == 'POST':
       form = LogInForm(request.POST)
       if form.is_valid():
           print(form.cleaned_data)
           return HttpResponseRedirect('/test')
       
   form = LogInForm()
   return render(request, 'Noclue/index.html',{
         'form': form})
   
   
def about(request):
    return render(request, 'Noclue/test.html')  