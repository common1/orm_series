from django.contrib.auth.models import User
from core.models import Restaurant, Rating, Sale
from django.utils import timezone
from django.db import connection
from pprint import pprint

def run():
  # 40 (Video 6)
  chinese = Restaurant.TypeChoices.CHINESE
  restaurants = Restaurant.objects.filter(restaurant_type=chinese)
  print(restaurants)
  print(connection.queries)

  # # 40 (Video 6)
  # restaurant = Restaurant.objects.filter(name='Jibberisch')
  # print(restaurant.exists())

  # # 40 (Video 6)
  # restaurant = Restaurant.objects.filter(restaurant_type=Restaurant.TypeChoices.ITALIAN)
  # print(restaurant.exists())

  # # 39 (Video 6)
  # restaurant = Restaurant.objects.filter(restaurant_type=Restaurant.TypeChoices.ITALIAN)
  # print(restaurant)

  # # 38 (Video 6)
  # restaurant = Restaurant.objects.get(name='Pizzeria 1')
  # print(restaurant)

  # # 37 (Video 6)
  # restaurant = Restaurant.objects.filter(name='Pizzeria 1')
  # print(restaurant)
  # print(restaurant.get())

  # # 36 (Video 6)
  # # Filter down to only chinese restaurants
  # print(Restaurant.objects.filter(name='Pizzeria 1'))
  # pprint(connection.queries)

  # # 35 (Video 6)
  # # Filter down to only chinese restaurants
  # print(Restaurant.objects.filter(restaurant_type=Restaurant.TypeChoices.CHINESE))
  # pprint(connection.queries)

  # # 34 (Video 6)
  # # Filter down to only chinese restaurants
  # print(Restaurant.objects.filter(restaurant_type=Restaurant.TypeChoices.CHINESE))
  # pprint(connection.queries)

  # # 33 (Video 6)
  # print(Restaurant.objects.count())
  # print(Rating.objects.count())
  # print(Sale.objects.count())
  # pprint(connection.queries)

  # # 32 (Video 5)
  # Restaurant.objects.all().delete()
  # pprint(connection.queries)

  # # 31 (Video 5)
  # restaurant = Restaurant.objects.first()
  # print(restaurant.delete())
  # pprint(connection.queries)

  # # 30 (Video 5)
  # restaurants = Restaurant.objects.filter(name__startswith='M')
  # print(restaurants)
  # print(restaurants.update(
  #   date_opened=timezone.now() - timezone.timedelta(days=365),
  #   website='https://test.com'
  # ))
  # pprint(connection.queries)

  # # 29 (Video 5)
  # restaurants = Restaurant.objects.all()
  # restaurants.update(
  #   date_opened=timezone.now()
  # )
  # pprint(connection.queries)

  # 28 (Video 5)
  # restaurant = Restaurant()
  # restaurant.name = 'My Italian Restaurant #5'
  # restaurant.date_opened = timezone.now()
  # restaurant.restaurant_type = Restaurant.TypeChoices.ITALIAN
  # restaurant.latitude = 50.2
  # restaurant.longitude = 50.2  
  # restaurant.save()
  # pprint(connection.queries)

  # # 27 (Video 5)
  # restaurant = Restaurant.objects.first()
  # print(restaurant.name)
  # restaurant.name = 'New Restaurant Name'
  # restaurant.save(update_fields=['name'])
  # print(restaurant.name)
  # pprint(connection.queries)

  # # 26 (Video 5)
  # restaurant = Restaurant  # pprint(connection.queries)
  # print(restaurant.name)
  # restaurant.name = 'New Restaurant Name'
  # restaurant.save()
  # print(restaurant.name)
  # pprint(connection.queries)
  
  # # 25 (Video 4
  # user = User.objects.first()
  # restaurant = Restaurant.objects.first()
  # rating = Rating.objects.create(
  #   user=user,
  #   restaurant=restaurant,
  #   rating=3   
  # )
  # rating.full_clean()
  # rating.save()

  # # 24
  # user = User.objects.first()
  # restaurant = Restaurant.objects.first()
  # rating = Rating.objects.create(
  #   user=user,
  #   restaurant=restaurant,
  #   rating=9    
  # )

  # # 23
  # user = User.objects.first()
  # restaurant = Restaurant.objects.first()
  # rating, created = Rating.objects.get_or_create(
  #   restaurant=restaurant,
  #   user=user,
  #   rating=4
  # )
  # if created:
  #   # send mail
  #   pass

  # # 23
  # user = User.objects.first()
  # restaurant = Restaurant.objects.first()
  # print(Rating.objects.get_or_create(
  #   restaurant=restaurant,
  #   user=user,
  #   rating=4
  # ))
  # pprint(connection.queries)
  
  # # 22
  # restaurant = Restaurant.objects.first()
  # print(restaurant.sales.all())
  
  # # 21
  # Sale.objects.create(
  #   restaurant= Restaurant.objects.first(),
  #   income=2.33,
  #   datetime=timezone.now()
  # )
  # Sale.objects.create(
  #   restaurant= Restaurant.objects.first(),
  #   income=5.33,
  #   datetime=timezone.now()
  # )
  # Sale.objects.create(
  #   restaurant= Restaurant.objects.first(),
  #   income=8.33,
  #   datetime=timezone.now()
  # )
  
  # # 20
  # retaurant = Restaurant.objects.first()
  # print(retaurant.ratings.all())
  
  # # 19
  # retaurant = Restaurant.objects.first()
  # print(retaurant.rating_set.all())
  
  # # 18
  # rating = Rating.objects.first()
  # print(rating.restaurant) 
  # print(connection.queries) 

  # # 17
  # restaurant = Restaurant.objects.first()
  # print(restaurant.name)
  # restaurant.name = 'jibberish'
  # restaurant.save()
  # print(connection.queries)  

  # # 16
  # print(Rating.objects.exclude(rating__lte=3))
  # print(connection.queries)  

  # # 15
  # print(Rating.objects.filter(rating__lte=3))
  # print(connection.queries)  

  # # 14
  # print(Rating.objects.filter(rating__gte=3))
  # print(connection.queries)  

  # # 13
  # print(Rating.objects.filter(rating=3))
  # print(connection.queries)  

  # # 12
  # print(Rating.objects.filter(rating=3))
  # print(Rating.objects.filter(rating=5))

  # # 11
  # print(Rating.objects.all())

  # # 010
  # restaurant = Restaurant.objects.first()
  # user = User.objects.first()
  
  # Rating.objects.create(
  #   user=user,
  #   restaurant=restaurant,
  #   rating=3
  # )
  
  # # 009
  # print(Restaurant.objects.last())  
  # print(connection.queries)  

  # # 008
  # print(Restaurant.objects.count())  
  # print(connection.queries)  

  # # 007
  # print(Restaurant.objects.all())  
  # print(connection.queries)  

  # # 006
  # Restaurant.objects.create(
  #   name="Pizza Shop",
  #   date_opened=timezone.now(),
  #   restaurant_type=Restaurant.TypeChoices.ITALIAN,
  #   latitude=50.2,
  #   longitude=50.5
  # )
  # print(connection.queries)  

  # # 005
  # restautant = Restaurant.objects.all()[0]
  # print(restautant)  
  # print(connection.queries)  

  # # 004
  # restautant = Restaurant.objects.first()
  # print(restautant)  
  # print(connection.queries)  

  # # 003
  # restautants = Restaurant.objects.all()
  # print(restautants)  
  # print(connection.queries)

  # # 002
  # restautants = Restaurant.objects.all()
  # print(restautants)

  # # 001
  # restaurant = Restaurant()
  # restaurant.name = 'My Italian Restaurant'
  # restaurant.latitude = 50.2
  # restaurant.longitude = 50.2
  # restaurant.date_opened = timezone.now()
  # restaurant.restaurant_type = Restaurant.TypeChoices.ITALIAN

  # restaurant.save()

