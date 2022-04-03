from multiprocessing import context
from django.forms import formset_factory
from django.shortcuts import render
from .models import InputModel
from .forms import InputForm

def index(request):
        form = formset_factory(InputForm)
        form_count = request.POST.get('form-TOTAL_FORMS')
        if request.method == 'POST':
            formset = form(request.POST)
            form = formset_factory(InputForm,extra=int(form_count))
            print(form_count)
            if formset.is_valid():
                model_input = InputModel(data=formset.cleaned_data)
                model_input.save()
        formset = form()
        context = {'formset': formset}
        return render(request, 'index.html', context)


def view(request):
        view_model = InputModel.objects.all()
        context = {'view_model': view_model}
        return render(request,'view.html',context)
