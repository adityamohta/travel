# travel

### Setting up project in local environment.

1) Create a virtual environment in your directory of choice.
   example - /webapps/travel_app/

```commandline
mkdir -p /webapps/travel_app
cd /webapps/travel_app/
virtualenv .
source bin/activate
git clone https://github.com/adityamohta/travel.git
cd travel
pip install -r requirements.txt
touch travel/settings/local.py
nano travel/settings/local.py
```

2) Add following code in local.py.
```python
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'travel',   # database name.
        'USER': 'username',     # username
        'PASSWORD': 'password',     # db password
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
* save file using ```ctrl + X```

* note : make sure you put in your local database credentials in local settings. 

3) Create migrations package.

* pwd - /webapps/travel_app/travel/
```commandline
mkdir /accounts/migrations
touch /accounts/migrations/__init__.py
mkdir /blog/migrations
touch /blog/migrations/__init__.py
mkdir /contactus/migrations
touch /contactus/migrations/__init__.py
mkdir /feedback/migrations
touch /feedback/migrations/__init__.py
mkdir /newsletter/migrations
touch /newsletter/migrations/__init__.py
mkdir /packages/migrations
touch /packages/migrations/__init__.py
```

4) Make Migrations and then run Migrate.

* pwd - /webapps/travel_app/travel/
```commandline
python manage.py makemigrations
python manage.py migrate
```

5) To runserver on localhost port 8000

* pwd - /webapps/travel_app/travel/
```commandline
python manage.py runserver
```
