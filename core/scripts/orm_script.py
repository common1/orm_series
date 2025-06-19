from django.contrib.auth.models import User
from core.models import Restaurant, Rating, Sale, Staff, StaffRestaurant
from django.utils import timezone
from django.db.models.functions import Upper, Length, Concat
from django.db import connection
from django.db.models import Count, Avg, Min, Max, Sum, StdDev, Variance, CharField, Value, F
from pprint import pprint
import random

def run():
  # 107
  rating = Rating.objects.filter(rating=3).first()
  rating.rating = F('rating') + 1
  rating.save()
  pprint(connection.queries)

# def run():
#   # 106
#   rating = Rating.objects.filter(rating=3).first()
#   rating.rating += 1
#   rating.save()
#   pprint(connection.queries)

# def run():
#   # 105
#   restaurants = Restaurant.objects.annotate(total_sales=Sum('sales__income')).filter(total_sales__lt=300)
#   print(restaurants.aggregate(avg_sales=Avg('total_sales')))
#   pprint(connection.queries)

# def run():
#   # 104
#   restaurants = Restaurant.objects.annotate(total_sales=Sum('sales__income')).filter(total_sales__lt=300)
#   for r in restaurants:
#     print(r.total_sales)
#   pprint(connection.queries)

# def run():
#   # 103
#   restaurants = Restaurant.objects.annotate(total_sales=Sum('sales__income')).order_by('-total_sales')
#   for r in restaurants:
#     print(r.total_sales)

# def run():
#   # 102
#   restaurants = Restaurant.objects.annotate(total_sales=Sum('sales__income')).order_by('total_sales')
#   for r in restaurants:
#     print(r.total_sales)

# def run():
#   # 101
#   restaurants = Restaurant.objects.annotate(total_sales=Sum('sales__income'))
#   for r in restaurants:
#     print(r.total_sales)

# def run():
#   # 100
#   restaurants = Restaurant.objects.values('restaurant_type').annotate(
#     num_ratings=Count('ratings')
#   )
#   print(restaurants)
#   pprint(connection.queries)

# def run():
#   # 99
#   restaurants = Restaurant.objects.annotate(
#     num_ratings=Count('ratings'),
#     avg_rating=Avg('ratings__rating')
#   )
#   print(restaurants.values('name', 'num_ratings', 'avg_rating'))

# def run():
#   # 98
#   restaurants = Restaurant.objects.annotate(num_ratings=Count('ratings'))
#   print(restaurants.values('name', 'num_ratings'))

# def run():
#   # 97
#   restaurants = Restaurant.objects.annotate(total_sales=Sum('sales__income')).values(
#     'name', 'total_sales'
#   )
#   print([r['total_sales'] for r in restaurants])
#   pprint(connection.queries)

# def run():
#   # 96
#   # Restaurant 1 [Rating: 4.3]
#   concatenation = Concat(
#     'name', Value(' [Rating: '), Avg('ratings__rating'), Value(']'),
#     output_field=CharField()
#   )
#   restaurants = Restaurant.objects.annotate(message=concatenation)
#   for r in restaurants:
#     print(r.message)

# def run():
#   #95
#   restaurants = Restaurant.objects.annotate(len_name=Length('name')).filter(
#     len_name__gt=10 # lte, lt, gt, gte
#   )
#   print(restaurants.values('name', 'len_name'))

# def run():
#   # 94
#   restaurants = Restaurant.objects.annotate(len_name=Length('name'))
#   print(restaurants.values('name', 'len_name'))

# def run():
#   # 93
#   # fetch all restaurants, end let's assume we want
#   # to get the number of characters in the name of the restaurant. so 'xyz' = 3.
#   restaurants = Restaurant.objects.annotate(len_name=Length('name'))
#   print(restaurants.first().len_name)

# def run():
#   # 92
#   one_month_ago = timezone.now() - timezone.timedelta(days=31)
#   sales = Sale.objects.filter(datetime__gte=one_month_ago)
#   print(sales.aggregate(
#       min=Min('income'),
#       max=Max('income'),
#       avg=Avg('income'),
#       sum=Sum('income'),
#   ))

# def run():
#   # 91
#   print(Sale.objects.aggregate(
#       min=Min('income'),
#       max=Max('income'),
#       avg=Avg('income'),
#       sum=Sum('income'),
#   ))

# def run():
#   # 90
#   print(Sale.objects.aggregate(
#       max=Max('income')
#   ))

# def run():
#   # 89
#   print(Sale.objects.aggregate(
#       min=Min('income')
#   ))

# def run():
#   # 88
#   print(Rating.objects.filter(restaurant__name__startswith='c').aggregate(avg=Avg('rating')))

# def run():
#   # 87
#   print(Rating.objects.aggregate(avg=Avg('rating')))

# def run():
#   # 86
#   print(Restaurant.objects.aggregate(total=Count('id')))
#   print(connection.queries)

# def run():
#   # 85
#   print(Restaurant.objects.filter(name__startswith='c').count())

# def run():
#   # 84
#   print(Restaurant.objects.count())

# def run():
#   # 83
#   restaurants = Restaurant.objects.values_list('latitude', flat=True)
#   print(restaurants)

# def run():
#   # 82
#   restaurants = Restaurant.objects.values_list('name', flat=True)
#   print(restaurants)

# def run():
#   # 81
#   restaurants = Restaurant.objects.values_list('name', 'date_opened')
#   print(restaurants)

# def run():
#   # 80
#   IT = Restaurant.TypeChoices.ITALIAN
#   ratings = Rating.objects.filter(restaurant__restaurant_type=IT).values('rating', 'restaurant__name')
#   print(ratings)
#   print(connection.queries)

# def run():
#   # 79
#   restaurants = Restaurant.objects.values(name_upper=Upper('name'))[:3]
#   print(restaurants)
#   print(connection.queries)

# def run():
#   # 78
#   restaurants = Restaurant.objects.values('name', 'date_opened')
#   print(restaurants)
#   print(connection.queries)

# def run():
#   # 77
#   restaurants = Restaurant.objects.values('name', 'date_opened').first()
#   print(restaurants['name'])

# def run():
#   # 76
#   restaurants = Restaurant.objects.values('name', 'date_opened').first()
#   print(restaurants)

# def run():
#   # 75
#   staff, created = Staff.objects.get_or_create(name='John Wick')
#   staff.restaurants.set(
#       Restaurant.objects.all()[:10],
#       through_defaults={'salary': random.randint(20_000, 80_000)}
#   )

# def run():
#   # 74
#   staff, created = Staff.objects.get_or_create(name='John Wick')
#   staff.restaurants.clear()
#   restaurant = Restaurant.objects.first()
#   staff.restaurants.add(restaurant, through_defaults={'salary': 28_000})

# def run():
#   # 73
#   staff, created = Staff.objects.get_or_create(name='John Wick')
#   restaurant = Restaurant.objects.first()
#   restaurant2 = Restaurant.objects.last()
#   staff_restaurants = StaffRestaurant.objects.filter(staff=staff)
#   for s in staff_restaurants:
#       print(s.salary)

# def run():
#   # 72
#   staff, created = Staff.objects.get_or_create(name='John Wick')
#   restaurant = Restaurant.objects.first()
#   restaurant2 = Restaurant.objects.last()
#   StaffRestaurant.objects.create(
#       staff=staff,
#       restaurant=restaurant,
#       salary=28_000
#   )
#   StaffRestaurant.objects.create(
#       staff=staff,
#       restaurant=restaurant2,
#       salary=24_000
#   )

# def run():
#   # 71
#   staff, created = Staff.objects.get_or_create(name='John Wick')
#   staff.restaurants.set(Restaurant.objects.all()[:20])
#   italian = staff.restaurants.filter(restaurant_type=Restaurant.TypeChoices.ITALIAN)
#   print(italian)

# def run():
#   # 70
#   staff, created = Staff.objects.get_or_create(name='John Wick')
#   staff.restaurants.clear()
#   print(staff.restaurants.count())

# def run():
#   # 69
#   staff, created = Staff.objects.get_or_create(name='John Wick')
#   staff.restaurants.set(Restaurant.objects.all()[:5])
#   print(staff.restaurants.count())

# def run():
#   # 68
#   staff, created = Staff.objects.get_or_create(name='John Wick')
#   staff.restaurants.remove(Restaurant.objects.first())
#   print(staff.restaurants.count())

# def run():
#   # 67
#   staff, created = Staff.objects.get_or_create(name='John Wick')
#   print(staff.restaurants.count())

# def run():
#   # 66
#   staff, created = Staff.objects.get_or_create(name='John Wick')
#   print(staff.restaurants.all())
#   staff.restaurants.add(Restaurant.objects.first())
#   print(staff.restaurants.all())

# def run():
#   # 65
#   chinese = Restaurant.TypeChoices.CHINESE
#   sales = Sale.objects.filter(restaurant__restaurant_type=chinese)
#   print(sales)
#   print(connection.queries)

# def run():
#   # 64
#   # find all ratings associated with a restaurant beginning with 'C'
#   ratings = Rating.objects.filter(restaurant__name__startswith='C')
#   print(ratings)
#   print(connection.queries)

# def run():
#   # 63
#   restaurant = Restaurant.objects.latest()
#   print(restaurant)
#   print(connection.queries)

# def run():
#   # 62
#   restaurant = Restaurant.objects.latest('date_opened')
#   print(restaurant)
#   print(connection.queries)

# def run():
#   # 61
#   restaurant = Restaurant.objects.earliest('date_opened')
#   print(restaurant)
#   print(connection.queries)

# def run():
#   # 60
#   restaurants = Restaurant.objects.order_by('date_opened')[2:5]
#   print(restaurants)
#   print(connection.queries)

# def run():
#   # 59
#   restaurants = Restaurant.objects.order_by('date_opened')[:5]
#   print(restaurants)
#   print(connection.queries)

# def run():
#   # 58
#   restaurants = Restaurant.objects.order_by('date_opened')[0]
#   print(restaurants)
#   print(connection.queries)

# def run():
#   # 57
#   restaurants = Restaurant.objects.order_by('date_opened')
#   print(restaurants)
#   print(connection.queries)

# def run():
#   # 56
#   restaurants = Restaurant.objects.order_by(Lower('name'))
#   print(restaurants)
#   print(connection.queries)

# def run():
#   # 55
#   sales = Sale.objects.order_by('-datetime')
#   print(sales)
#   print(connection.queries)

# def run():
#   # 54
#   restaurants = Restaurant.objects.order_by('-name')
#   print(restaurants)
#   print(connection.queries)

# def run():
#   # 53
#   restaurants = Restaurant.objects.order_by('name').reverse()
#   print(restaurants)
#   print(connection.queries)

# def run():
#   # 52
#   sales = Sale.objects.filter(income__range=(50, 60))
#   print([sale.income for sale in sales])
#   print(connection.queries)

# def run():
#   # 51
#   sales = Sale.objects.filter(income__gt=90)
#   print(sales)
#   print(connection.queries)

# def run():
#   # 50
#   restaurants = Restaurant.objects.filter(longitude__lt=0)
#   print(restaurants)
#   print(connection.queries)

# def run():
#   # 49
#   restaurants = Restaurant.objects.exclude(longitude__gt=0)
#   print(restaurants)
#   print(connection.queries)

# def run():
#   # 48
#   restaurants = Restaurant.objects.filter(longitude__gt=0)
#   print(restaurants)
#   print(connection.queries)

# def run():
#   # 47
#   restaurants = Restaurant.objects.filter(name__lt='E')
#   print(restaurants)
#   print(connection.queries)

# def run():
#   # 46
#   chinese = Restaurant.TypeChoices.CHINESE
#   indian = Restaurant.TypeChoices.INDIAN
#   restaurants = Restaurant.objects.exclude(restaurant_type__in=[chinese, indian])
#   print(restaurants)
#   print(connection.queries)

# def run():
#   # 45
#   chinese = Restaurant.TypeChoices.CHINESE
#   restaurants = Restaurant.objects.exclude(restaurant_type=chinese)
#   print(restaurants)
#   print(connection.queries)

# def run():
#   # 44
#   chinese = Restaurant.TypeChoices.CHINESE
#   indian = Restaurant.TypeChoices.index
#   mexican = Restaurant.TypeChoices.MEXICAN
#   checktypes = [chinese, indian, mexican]
#   restaurants  = Restaurant.objects.filter(restaurant_type__in=checktypes)
#   print(restaurants)
#   print(connection.queries)

# def run():
#   # 43
#   chinese = Restaurant.TypeChoices.CHINESE
#   restaurants = Restaurant.objects.filter(restaurant_type=chinese, name__startswith='C')
#   print(restaurants)
#   print(connection.queries)

# def run():
#   # 42
#   restaurant = Restaurant.objects.filter(name='Jibberisch')
#   print(restaurant.exists())

# def run():
#   # 41
#   restaurant = Restaurant.objects.filter(restaurant_type=Restaurant.TypeChoices.ITALIAN)
#   print(restaurant.exists())

# def run():
#   # 40
#   restaurant = Restaurant.objects.filter(restaurant_type=Restaurant.TypeChoices.ITALIAN)
#   print(restaurant)

# def run():
#   # 39
#   restaurant = Restaurant.objects.get(name='Pizzeria 1')
#   print(restaurant)

# def run():
#   # 38
#   restaurant = Restaurant.objects.filter(name='Pizzeria 1')
#   print(restaurant)
#   print(restaurant.get())

# def run():
#   # 37
#   # Filter down to only chinese restaurants
#   print(Restaurant.objects.filter(name='Pizzeria 1'))
#   pprint(connection.queries)

# def run():
#   # 36
#   # Filter down to only chinese restaurants
#   print(Restaurant.objects.filter(restaurant_type=Restaurant.TypeChoices.CHINESE))
#   pprint(connection.queries)

# def run():
#   # 35
#   # Filter down to only chinese restaurants
#   print(Restaurant.objects.filter(restaurant_type=Restaurant.TypeChoices.CHINESE))
#   pprint(connection.queries)

# def run():
#   # 34
#   print(Restaurant.objects.count())
#   print(Rating.objects.count())
#   print(Sale.objects.count())
#   pprint(connection.queries)

# def run():
  # # 33 (Video 5)
  # Restaurant.objects.all().delete()
  # pprint(connection.queries)

# def run():
#   # 32 (Video 5)
#   restaurant = Restaurant.objects.first()
#   print(restaurant.delete())
#   pprint(connection.queries)

# def run():
#   # 31 (Video 5)
#   restaurants = Restaurant.objects.filter(name__startswith='M')
#   print(restaurants)
#   print(restaurants.update(
#   date_opened=timezone.now() - timezone.timedelta(days=365),
#   website='https://test.com'
#   ))
#   pprint(connection.queries)

# def run():
#   # 30 (Video 5)
#   restaurants = Restaurant.objects.all()
#   restaurants.update(
#   date_opened=timezone.now()
#   )
#   pprint(connection.queries)

# def run():
#   # 29 (Video 5)
#   restaurant = Restaurant()
#   restaurant.name = 'My Italian Restaurant #5'
#   restaurant.date_opened = timezone.now()
#   restaurant.restaurant_type = Restaurant.TypeChoices.ITALIAN
#   restaurant.latitude = 50.2
#   restaurant.longitude = 50.2
#   restaurant.save()
#   pprint(connection.queries)

# def run():
#   # 28 (Video 5)
#   restaurant = Restaurant.objects.first()
#   print(restaurant.name)
#   restaurant.name = 'New Restaurant Name'
#   restaurant.save(update_fields=['name'])
#   print(restaurant.name)
#   pprint(connection.queries)

# def run():
#   # 27 (Video 5)
#   restaurant = Restaurant  # pprint(connection.queries)
#   print(restaurant.name)
#   restaurant.name = 'New Restaurant Name'
#   restaurant.save()
#   print(restaurant.name)
#   pprint(connection.queries)

# def run():
#   # 26 (Video 4
#   user = User.objects.first()
#   restaurant = Restaurant.objects.first()
#   rating = Rating.objects.create(
#   user=user,
#   restaurant=restaurant,
#   rating=3
#   )
#   rating.full_clean()
#   rating.save()

# def run():
#   # 25
#   user = User.objects.first()
#   restaurant = Restaurant.objects.first()
#   rating = Rating.objects.create(
#   user=user,
#   restaurant=restaurant,
#   rating=9
#   )

# def run():
#   # 24
#   user = User.objects.first()
#   restaurant = Restaurant.objects.first()
#   rating, created = Rating.objects.get_or_create(
#   restaurant=restaurant,
#   user=user,
#   rating=4
#   )
#   if created:
#   # send mail
#   pass

# def run():
#   # 23
#   user = User.objects.first()
#   restaurant = Restaurant.objects.first()
#   print(Rating.objects.get_or_create(
#   restaurant=restaurant,
#   user=user,
#   rating=4
#   ))
#   pprint(connection.queries)

# def run():
#   # 22
#   restaurant = Restaurant.objects.first()
#   print(restaurant.sales.all())

# def run():
#   # 21
#   Sale.objects.create(
#   restaurant= Restaurant.objects.first(),
#   income=2.33,
#   datetime=timezone.now()
#   )
#   Sale.objects.create(
#   restaurant= Restaurant.objects.first(),
#   income=5.33,
#   datetime=timezone.now()
#   )
#   Sale.objects.create(
#   restaurant= Restaurant.objects.first(),
#   income=8.33,
#   datetime=timezone.now()
#   )

# def run():
#   # 20
#   retaurant = Restaurant.objects.first()
#   print(retaurant.ratings.all())

# def run():
#   # 19
#   retaurant = Restaurant.objects.first()
#   print(retaurant.rating_set.all())

# def run():
#   # 18
#   rating = Rating.objects.first()
#   print(rating.restaurant)
#   print(connection.queries)

# def run():
#   # 17
#   restaurant = Restaurant.objects.first()
#   print(restaurant.name)
#   restaurant.name = 'jibberish'
#   restaurant.save()
#   print(connection.queries)

# def run():
#   # 16
#   print(Rating.objects.exclude(rating__lte=3))
#   print(connection.queries)

# def run():
#   # 15
#   print(Rating.objects.filter(rating__lte=3))
#   print(connection.queries)

# def run():
#   # 14
#   print(Rating.objects.filter(rating__gte=3))
#   print(connection.queries)

# def run():
#   # 13
#   print(Rating.objects.filter(rating=3))
#   print(connection.queries)

# def run():
#   # 12
#   print(Rating.objects.filter(rating=3))
#   print(Rating.objects.filter(rating=5))

# def run():
#   # 11
#   print(Rating.objects.all())

# def run():
#   # 010
#   restaurant = Restaurant.objects.first()
#   user = User.objects.first()
#   Rating.objects.create(
#   user=user,
#   restaurant=restaurant,
#   rating=3
#   )

# def run():
#   # 009
#   print(Restaurant.objects.last())
#   print(connection.queries)

# def run():
#   # 008
#   print(Restaurant.objects.count())
#   print(connection.queries)

# def run():
#   # 007
#   print(Restaurant.objects.all())
#   print(connection.queries)

# def run():
#   # 006
#   Restaurant.objects.create(
#   name="Pizza Shop",
#   date_opened=timezone.now(),
#   restaurant_type=Restaurant.TypeChoices.ITALIAN,
#   latitude=50.2,
#   longitude=50.5
#   )
#   print(connection.queries)

# def run():
#   # 005
#   restautant = Restaurant.objects.all()[0]
#   print(restautant)
#   print(connection.queries)

# def run():
#   # 004
#   restautant = Restaurant.objects.first()
#   print(restautant)
#   print(connection.queries)

# def run():
#   # 003
#   restautants = Restaurant.objects.all()
#   print(restautants)
#   print(connection.queries)

# def run():
#   # 002
#   restautants = Restaurant.objects.all()
#   print(restautants)

# def run():
#   # 001
#   restaurant = Restaurant()
#   restaurant.name = 'My Italian Restaurant'
#   restaurant.latitude = 50.2
#   restaurant.longitude = 50.2
#   restaurant.date_opened = timezone.now()
#   restaurant.restaurant_type = Restaurant.TypeChoices.ITALIAN
#   restaurant.save()

