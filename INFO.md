# orm_series

## See also

[https://www.youtube.com/playlist?list=PL-2EBeDYMIbTT7ri4pNEBu9VoVSAkOvd2]

[https://github.com/bugbytes-io/django-orm-series]

## 001 Django ORM Deep Dive - Models, Migrations and Admin UI Integration

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


