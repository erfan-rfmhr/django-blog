from django.contrib.auth import forms
from django.urls import reverse_lazy
from django.views import generic


# Create your views here.
class SignUpView(generic.CreateView):
    form_class = forms.UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
