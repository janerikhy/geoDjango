from .forms import CSUserSingUpForm, ScientistSignUpForm
from django.views.generic import DetailView, CreateView, TemplateView
from observations.models import ObservationTest
from .models import CitizenScientist, Scientist
from django.urls import reverse_lazy


# Create your views here.


class SignUpView(TemplateView):
    template_name = "users/signup.html"


class CreateCSUserView(CreateView):
    model = CitizenScientist
    form_class = CSUserSingUpForm
    template_name = 'users/create_user.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'citizen scientist'
        return super().get_context_data(**kwargs)


class CreateResearcherView(CreateView):
    model = Scientist
    form_class = ScientistSignUpForm
    template_name = "users/create_user.html"
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = "scientist"
        return super().get_context_data(**kwargs)
