from django.core.paginator import Paginator
from django.shortcuts import render
from django.db.models import Q

from .models import DjResult, DjRunner


def results(request):
    item_list = DjResult.objects.all()

    # Get the search term from the request GET parameters
    search_term = request.GET.get('q')

    # Get the filter values from the request GET parameters
    dist_from = request.GET.get('dist_from')
    dist_to = request.GET.get('dist_to')
    dob_from = request.GET.get('dob_from')
    dob_to = request.GET.get('dob_to')
    result_from = request.GET.get('result_from')
    result_to = request.GET.get('result_to')

    if search_term and search_term != 'None':
        item_list = item_list.filter(lname__icontains=search_term) | \
                    item_list.filter(fname__icontains=search_term)

    if dist_from and dist_from != 'None':
        item_list = item_list.filter(race__dist__gte=float(dist_from))
    if dist_to and dist_to != 'None':
        item_list = item_list.filter(race__dist__lte=float(dist_to))

    if dob_from and dob_from != 'None':
        item_list = item_list.filter(runner__birthday__gte=dob_from)
    if dob_to and dob_to != 'None':
        item_list = item_list.filter(runner__birthday__lte=dob_to)

    if result_from and result_from != 'None':
        item_list = item_list.filter(time_raw__gte=float(result_from))
    if result_to and result_to != 'None':
        item_list = item_list.filter(time_raw__lte=float(result_to))

    item_list = item_list.order_by('time_raw')

    paginator = Paginator(item_list, 25)  # Show 25 items per page

    page = request.GET.get('page')
    items = paginator.get_page(page)

    return render(request, "table.html", {
        'items': items,
        'search_term': search_term,
        'dist_from': dist_from,
        'dist_to': dist_to,
        'dob_from': dob_from,
        'dob_to': dob_to,
        # 'result_from': result_from,
        # 'result_to': result_to,
    })


def unique_users(request):
    search_term = request.GET.get('q')
    if search_term and search_term != 'None':
        users = DjRunner.objects.filter(Q(lname__icontains=search_term) | Q(fname__icontains=search_term)).order_by(
            '-birthday')
    else:
        users = []

    return render(request, "unique_users.html", {'users': users, 'search_term': search_term})


def home(request):
    return render(request, "home.html")
