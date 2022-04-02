from django.forms import modelformset_factory
from django.shortcuts import render
from .models import InputModel

def index(request):
        model_formset = modelformset_factory(InputModel,fields=({'data':''}),extra=1)
        if request.method == "POST":
               form = model_formset(request.POST)
               form.save()
        form = model_formset()  
        return render(request,'index.html',{'form':form}) 


def view(request):
        view_model = InputModel.objects.all()
        context = {'view_model': view_model}
        return render(request,'view.html',context)