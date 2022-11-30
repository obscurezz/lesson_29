## Create postgres container

`docker run --name hw_28_pg -e POSTGRES_PASSWORD=hw_28_postgres -p 5432:5432 -d postgres`

## Migrate database

`python manage.py migrate`

## Load fixtures

`python manage.py loaddata loaddata/*`

***
### Search filters in ads view

> By category name: ?category=

> By ad name: ?name=

> By user location: ?location=

> By price range: ?price_from= ?price_to=
***
### Tests

`python -m pytest -vv tests/`
***