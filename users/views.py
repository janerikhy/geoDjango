from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from .forms import CustomUserCreationForm, UserForm
from django.views.generic import DetailView, CreateView
from observations.models import ObservationTest
from .models import CitizenScientist
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.


class CreateUserView(CreateView):
    model = CitizenScientist
    form_class = UserForm
    template_name = 'users/create_user.html'
    success_url = reverse_lazy('home')


# Must add some sort of restriction so that one have to be logged in to access the profile
# Also the query is wrong at this point, only the data related to the logged in user is showing
# must be changed to some sort of relation to the user profile

class ProfileView(DetailView):
    model = CitizenScientist
    template_name = 'users/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(kwargs['object'].pk)
        print(self.request.user)
        obs = ObservationTest.objects.filter(user__user=self.request.user)
        numb_observations = []
        data = []
        data_dict = {}
        for i in range(len(obs)):
            numb_observations.append(len(ObservationTest.objects.filter(
                obs_date__date=obs[i].obs_date.date(), user__user=self.request.user)))
            data.append(obs[i].obs_date.date())
            data_dict[obs[i].obs_date.date()] = numb_observations[i]
        context['data'] = data
        context['numb_observations'] = numb_observations
        context['plot'] = data_dict
        context['observations'] = ObservationTest.objects.filter(
            user__user=self.request.user)
        return context


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
