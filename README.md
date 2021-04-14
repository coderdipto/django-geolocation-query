# Django Geolocation Query


### Implemented 

- Mapbox
- PostgreSQL + PointField
- Django geolocation queries


### Used Django ORM Queries

```python
// Getting cities within 100 km radius

from django.contrib.gis.measure import D
from django.contrib.gis.geos import Point

Location.objects.filter(point__distance_lte(current_location, D(km=100)))
```

```python
// Getting nearby top 10 cities sorted by distance within 200 KM radius

from django.contrib.gis.measure import D
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance

Location.objects.filter(point__distance_lte=(current_location, D(km=200))).annotate(distance=Distance("point", point)).order_by("distance")[:10]

```

### How to use

Clone the repository.

```sh
git clone git@github.com:coderdipto/django-geolocation-query.git
```

Create and activate a virtual environment for the project.

For creating virtual environment we can use packages like [Virtualenv](https://pypi.org/project/virtualenv/) or [Pyenv](https://github.com/pyenv/pyenv). I've used Virtualenv.

```sh
cd django-geolocation-query
virtualenv venv
source venv/bin/activte
```
Install all required packages.

```sh
pip install -r requirements.txt # Required
pip install -r requirements.dev.txt # Only required for development
pip install -r requirements.prod.txt # Only required for production
```
Create a `.env` file copying from `.env.keep` file and update these values.
```env
# Comma separated hosts or IPs, set * to allow all 
ALLOWED_HOSTS=192.168.0.1,www.example.com 

# In production DEBUG should be False, in development it can be set to True
DEBUG=True 

# Secret key should be atleast 32 characters long and consists of alphanumeric and special characters
SECRET_KEY=**** 

# See django database URL documentation for other databases
DB_URL=postgres://USER:PASSWORD@HOST:PORT/NAME 

TEST_DB_URL=postgres://USER:PASSWORD@HOST:PORT/NAME
```

Run migrations.
```sh
python manage.py migrate
```

Seed data.
```sh
python manage.py seed
```

Run the project.
```sh
python manage.py runserver
```

### Preview
![Preview](https://i.imgur.com/a4ecrdK.png)