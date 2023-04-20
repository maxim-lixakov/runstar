from django.core.paginator import Paginator
from django.shortcuts import render

from .models import DjResult


def results(request):
    item_list = DjResult.objects.all()

    # Get the search term from the request GET parameters
    search_term = request.GET.get('q')

    if search_term and search_term != 'None':
        item_list = item_list.filter(lname__icontains=search_term) | \
                item_list.filter(fname__icontains=search_term)

    paginator = Paginator(item_list, 25)  # Show 25 items per page

    page = request.GET.get('page')
    items = paginator.get_page(page)

    return render(request, "table.html", {'items': items, 'search_term': search_term})


def home(request):
    return render(request, "home.html")