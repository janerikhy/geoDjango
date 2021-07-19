from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from .forms import CitizenScientistForm, CustomUserCreationForm, UserForm
from django.views.generic import DetailView, CreateView
from .models import CitizenScientist
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.


class CreateUserView(CreateView):
    model = CitizenScientist
    form_class = UserForm
    template_name = 'users/create_user.html'
    success_url = reverse_lazy('home')


def register(request):
    if request.method == "POST":
        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('home')
    else:
        f = CustomUserCreationForm()
    return render(request, 'users/create_user.html', {'form': f})
