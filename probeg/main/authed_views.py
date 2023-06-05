from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from scipy import interpolate

from .models import DjResult, DjRunner
from .forms import CreationForm


# create interpolation function
y = [800, 1000, 1500, 3000, 5000, 10000, 21100, 42200]
x = [116, 148, 235, 510, 880, 1850, 4140, 8910]
f2 = interpolate.interp1d(x, y, kind = 'cubic', fill_value="extrapolate")


class SignUp(CreateView):
    form_class = CreationForm
    # После успешной регистрации перенаправляем пользователя на главную.
    success_url = reverse_lazy('home')
    template_name = 'registration/signup.html'


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


        # create graph
        time_objs = []
        dist_objs = []
        dates = []
        metrics = []

        try:
            for result in DjResult.objects.filter(runner=runner.id).order_by('added_time').distinct():
                if float(result.race.dist) < 43 and  float(result.race.dist) > 0.6:
                    components = result.time_raw.split(':')
                    if len(components) == 3:
                        hours = int(components[0])
                        minutes = int(components[1])
                        seconds_milliseconds = components[2].split('.')
                        if len(seconds_milliseconds) == 2:
                            seconds = int(seconds_milliseconds[0])
                            milliseconds = int(seconds_milliseconds[1])
                        else:
                            print("Invalid input. The string does not match the expected format.")
                            continue
                    elif len(components) == 2:
                        minutes = int(components[0])
                        seconds_milliseconds = components[1].split('.')
                        if len(seconds_milliseconds) == 2:
                            seconds = int(seconds_milliseconds[0])
                            milliseconds = int(seconds_milliseconds[1])
                        else:
                            print("Invalid input. The string does not match the expected format.")
                            continue
                    else:
                        print("Invalid input. The string does not match the expected format.")
                        continue
                    seconds = (hours * 3600) + (minutes * 60) + seconds + (milliseconds / 1000)
                    metric = float(result.race.dist*1000)/f2(seconds)
                    if metric < 2:
                        time_objs.append(seconds)
                        dist_objs.append(result.race.dist*1000)
                        dates.append(result.added_time.strftime("%Y-%m-%d"))
                        metrics.append(float(result.race.dist*1000)/f2(seconds))
        except ValueError:
            print(f'GOT VALUE ERROR for user with id: {uid}')

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
            "labels": dates,
            "values": metrics,
        }
        return render(request, 'profile.html', context)
    else:
        return render(request, 'profile.html', {})
