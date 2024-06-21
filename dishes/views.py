from django.shortcuts import render
from .models import Dish
from django.db.models import Q


def search_dishes(request):
    query = request.GET.get("q")
    if query:
        dishes = Dish.objects.filter(Q(name__icontains=query)).distinct()
    else:
        dishes = []
    return render(request, "search.html", {"dishes": dishes, "query": query})
