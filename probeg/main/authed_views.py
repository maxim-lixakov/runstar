from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.models import Group, User
from django.views.generic import CreateView
from wagtail.models import Page

from .models import DjResult, DjRunner
from .forms import CreationForm


class SignUp(CreateView):
    form_class = CreationForm
    # После успешной регистрации перенаправляем пользователя на главную.
    success_url = reverse_lazy('home')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        form.instance.save()
        group = Group.objects.get(name="Users")
        group.user_set.add(form.instance)
        return super(CreateView, self).form_valid(form)



# @login_required
def profile(request):
    uid = request.GET.get('id', 0)
    current_user = request.user

    runner = DjRunner.objects.filter(id=uid).first()
    pages = Page.objects.filter(owner_id=current_user.id).all()
    print([page.url_path for page in pages])
    return render(request, 'profile.html', {'runner': runner, 'pages': pages})
