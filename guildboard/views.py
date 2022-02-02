from audioop import reverse
from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .models import *
# Create your views here.

class CustomLoginView(LoginView):
    template_name = "guildboard/login.html"
    fields = "__all__"
    redirect_authenticate_user = True

    def get_success_url(self):
        return reverse_lazy("index")

def index(request):
    return render(request, "guildboard/index.html")

