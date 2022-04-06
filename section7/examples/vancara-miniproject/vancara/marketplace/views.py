from django.shortcuts import render
from django.shortcuts import render

from .models import Vehicle

from django.core.paginator import Paginator


# Create your views here.



def render_with_pagination(request, vehicles, show_something):

    page_num = request.GET.get('page', 1)
    paginator = Paginator(vehicles, per_page=2)
    cars = paginator.page(page_num)

    return render(request, "marketplace/index.html", {'page': cars,'show_something': show_something})



def index(request):
    vehicles = Vehicle.objects.all()
    return render_with_pagination(request, vehicles, True)


def make(request, id):
    vehicles = Vehicle.objects.filter(make__id=id)
    return render_with_pagination(request, vehicles, False)