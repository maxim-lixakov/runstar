from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import DjResult, DjRunner
from .forms import CreationForm


class SignUp(CreateView):
    form_class = CreationForm
    # После успешной регистрации перенаправляем пользователя на главную.
    success_url = reverse_lazy('home')
    template_name = 'registration/signup.html'


# @login_required
def profile(request):
    uid = request.GET.get('id', 0)

    runner = DjRunner.objects.filter(id=uid).first()

    return render(request, 'profile.html', {'runner': runner})
