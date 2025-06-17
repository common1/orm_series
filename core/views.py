from django.shortcuts import render
from .forms import RestaurantForm
from core.models import Restaurant, Sale, Rating
from django.db.models import Sum
from django.utils import timezone

# 4
def index(request):
    # Get all 5-star ratings, and fetch all the sales for restaurants with 5-star raging.
    month_ago = timezone.now() - timezone.delta(days=30)
    restaurants = Restaurant.objects.prefetch_related('ratings', 'sales').filter(ratings__rating=5)
    print(restaurants)
    return render(request, 'index.html')

# # 4
# def index(request):
#     # Get all 5-star ratings, and fetch all the sales for restaurants with 5-star raging.
#     restaurants = Restaurant.objects.prefetch_related('ratings', 'sales') \
#         .filter(ratings__rating=5) \
#         .annotate(total=Sum('sales__income'))
#     print(restaurants)
#     return render(request, 'index.html')

# # 3
# def index(request):
#     ratings = Rating.objects.only('rating', 'restaurant__name').select_related('restaurant')
#     context = {'ratings': ratings}
#     return render(request, 'index.html', context)

# # 2
# def index(request):
#     ratings = Rating.objects.select_related('restaurant')
#     context = {'ratings': ratings}
#     return render(request, 'index.html', context)

# # 1
# def index(request):
#     restaurants = Restaurant.objects.filter(name__istartswith='c').prefetch_related('ratings', 'sales')
#     context = {'restaurants': restaurants}
#     return render(request, 'index.html', context)
