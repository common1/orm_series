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

