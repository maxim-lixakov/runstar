from django.core.paginator import Paginator
from django.shortcuts import render

from .models import DjResult


def index(request):
    item_list = DjResult.objects.all()
    paginator = Paginator(item_list, 25)  # Show 25 items per page

    page = request.GET.get('page')
    items = paginator.get_page(page)

    return render(request, "table.html", {'items': items})