from django.shortcuts import render 
from django.http import HttpResponseRedirect
from .forms import LogInForm
from django.views import View

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

def about(request):
    return render(request, 'Noclue/test.html')
