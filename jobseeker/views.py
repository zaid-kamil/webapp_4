from django.shortcuts import render, redirect
from .models import Person
from .forms import PersonForm   
from django.contrib import messages

# Create your views here.

def home(request):
    # add person form
    form = PersonForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save() # save the form data to model
            messages.success(request, 'Your details added successfully')
            return redirect('home')
        else:
            messages.error(request, 'Error adding your details')
    ctx = {'form': form}
    return render(request, 'jobseeker/home.html', ctx)