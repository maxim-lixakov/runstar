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

    class BestResult:

        def __init__(self, dist, result):
            self.dist = dist
            self.result = result

    uid = request.GET.get('id', 0)
    runner = DjRunner.objects.filter(id=uid).first()

    if runner:

        # Get the best results for all distances for the current runner
        results = DjResult.objects.filter(runner=runner.id).order_by('race__dist', '-time_raw').distinct()

        # Create a dictionary to store the best results by distance
        best_results = {}
        for result in results:
            if float(result.race.dist) < 43:
                if result.race.dist in best_results:
                    best_results[float(result.race.dist)].append(result.time_raw)
                else:
                    best_results[float(result.race.dist)] = [result.time_raw]

        # Get a list of all the distances in the best_results dictionary
        distances = list(best_results.keys())

        # Render the updated profile page template with the runner and results data
        pbs = []
        for res in best_results:
            pb = BestResult(res, best_results[res][-1])
            pbs.append(pb)

        context = {
            'runner': runner,
            'distances': distances,
            'best_results': pbs,
            'n': len(distances),
        }
        return render(request, 'profile.html', context)
    else:
        return render(request, 'profile.html', {})
