### Set up your local virtual env with virtualenv

`virtualenv venv`

`source venv/bin/activate`

`pip install -r requirements.txt`

### Set up your local environment variables

Add your nutrix api key and api_id to sample.env and rename sample.env to .env

`mv sample.env .env`

### Set up your database and create a super user

`python manage.py migrate`

`python manage.py createsuperuser`


### Load initial product data with upcs with a management command

`python manage.py load_initial_data`


### Run locally with heroku toolbelt

Install here https://toolbelt.heroku.com/

`heroku local`



# Capital Area Foodbank UPC Scanner Site and backend

### Data to be investigated then parsed and cleaned

http://us.openfoodfacts.org/data

http://www.mynetdiary.com/food-database.html


### Mobile App to be refactored


#### Use this as a starting point
https://github.com/openfoodfacts/openfoodfacts-android/tree/master/phonegap/Open%20Food%20Facts


### To Do Items:

Add Captcha for form

https://github.com/praekelt/django-recaptcha

heroku config:add BUILDPACK_URL=https://github.com/amanjain/heroku-buildpack-python-with-django-bower.git

heroku config:add api_key=(insert nutrix api key here)
heroku config:add api_id=(insert nutrix api id here)

### Load initial Data

`python manage.py load_initial_data`


### REST API

No tokens or keys required for this version of the API

#### Listview of all UPCs in DB so far
https://cafbsite.herokuapp.com/api/

#### Query Products UPCs already in the DB
https://cafbsite.herokuapp.com/api/auth/upc=52009830171/?format=json

Should return {"gtin_code":"52009830171","gtin_name":"Honey","created":"2016-03-06T04:34:59.001637Z"}
