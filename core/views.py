from django.shortcuts import render
from .forms import RestaurantForm
from core.models import Restaurant, Sale, Rating
from django.db.models import Sum, Prefetch
from django.utils import timezone

# 4
def index(request):
    # Get all 5-star ratings, and fetch all the sales for restaurants with 5-star raging.
    month_ago = timezone.now() - timezone.timedelta(days=30)
    monthly_sales = Prefetch(
        'sales',
        queryset=Sale.objects.filter(datetime__gte=month_ago)
    )
    restaurants = Restaurant.objects.prefetch_related('ratings', monthly_sales).filter(ratings__rating=5)
    restaurants = restaurants.annotate(total=Sum('sales__income'))
    print([r.total for r in restaurants])
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
