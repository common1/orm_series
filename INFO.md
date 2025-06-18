# orm_series

## See also

[https://www.youtube.com/playlist?list=PL-2EBeDYMIbTT7ri4pNEBu9VoVSAkOvd2]

[https://github.com/bugbytes-io/django-orm-series]

## 001 Django ORM Deep Dive - Models, Migrations and Admin UI Integration

[https://www.youtube.com/watch?v=t7diJPGxCGo&list=PL-2EBeDYMIbQXKsyNweppuFptuogJe2L-&index=2]

```
$ mkdir orm_series
$ cd orm_series
$ python3 -m venv .venv
$ source .venv/bin/activae
$ pip install django django-extensions
$ django-admin startproject orm_series .
$ python manage.py startapp core

File: orm-esries/settings.py
INSTALLED_APPS = [
    ...
    'django_extensions',
    'core',
]
$ python mange.py makemigrations
$ python mange.py migrate

$ python manage.py createsuperuser
ubuntuuser
ubuntuuser@ubuntuserver.com

```

## 002 Django ORM - Querying and Creating Records / Working with Foreign Keys

[https://www.youtube.com/watch?v=46au1MxtOJE&list=PL-2EBeDYMIbQXKsyNweppuFptuogJe2L-&index=3]

# 003 Django ORM - Model Field Validators / Writing Custom Validators / ModelForms

[https://www.youtube.com/watch?v=1x0Zdukpjrs&list=PL-2EBeDYMIbQXKsyNweppuFptuogJe2L-&index=4]

# 004 Django ORM - Updating and Deleting QuerySets / ForeignKey on_delete behaviour - Part 1

[https://www.youtube.com/watch?v=cN4zjbcM2kk&list=PL-2EBeDYMIbQXKsyNweppuFptuogJe2L-&index=5]

# 004 Django ORM - Updating and Deleting QuerySets / ForeignKey on_delete behaviour - Part 2

...

# 005 Django ORM - QuerySet Filtering and Lookups / Ordering and Slicing QuerySets - Part 1

[https://www.youtube.com/watch?v=84BBAGEu064&list=PL-2EBeDYMIbQXKsyNweppuFptuogJe2L-&index=6]

```
$ python manage.py createdata
```

# 005 Django ORM - QuerySet Filtering and Lookups / Ordering and Slicing QuerySets - Part 2

...

# 005 Django ORM - QuerySet Filtering and Lookups / Ordering and Slicing QuerySets - Part 3

...

# 005 Django ORM - QuerySet Filtering and Lookups / Ordering and Slicing QuerySets - Part 4

...

# 006 Django Query Optimization / select_related & prefetch_related / django-debug-toolbar / N+1 Problem - Part 1

[https://www.youtube.com/watch?v=a3dTy8RO5Ho&list=PL-2EBeDYMIbQXKsyNweppuFptuogJe2L-&index=7]
[https://django-debug-toolbar.readthedocs.io/en/latest/installation.html]

```
$ pip install django-debug-toolbar

File: orm_series/settings.py
INSTALLED_APPS = [
    ...
    'debug_toolbar',
]
...
MIDDLEWARE = [
    ...
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    ...
]
...
INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]

File: orm_series/urls.py
urlpatterns = [
    ...
    path('__debug__/', include("debug_toolbar.urls")),
]

```

# 006 Django Query Optimization / select_related & prefetch_related / django-debug-toolbar / N+1 Problem - Part 2

...

# 006 Django Query Optimization / select_related & prefetch_related / django-debug-toolbar / N+1 Problem - Part 3

...

