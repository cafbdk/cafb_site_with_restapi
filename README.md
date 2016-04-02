# Capital Area Foodbank Site and Backend
## Set Up Instructions to get developing

### Set up a project directory with git

`mkdir cafb_site`

`cd cafb_site`

`git clone https://github.com/cafbdk/cafb_site_with_restapi.git`

`cd cafb_site_with_restapi`

### Set up your local virtual env with [virtualenv](https://virtualenv.pypa.io/en/latest/)

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


### Check it out locally (default options)

Open http://localhost:5000/ in your browser


# Deploying to Heroku

`heroku create`

`heroku config:add BUILDPACK_URL=https://github.com/amanjain/heroku-buildpack-python-with-django-bower.git`

`heroku config:add api_key=(insert nutrix api key here)`

`heroku config:add api_id=(insert nutrix api id here)``

`git push heroku master`

### Set up your database and create a super user

`heroku run python manage.py migrate`

`heroku run python manage.py createsuperuser`

### Load initial Data (if you want)

`heroku run python manage.py load_initial_data`


### Checkout if your site is live and working!

`heroku open`


# REST API

No tokens or keys required for this version of the API

#### Listview of all UPCs in DB so far
https://cafbsite.herokuapp.com/api/

#### Query Products UPCs already in the DB
https://cafbsite.herokuapp.com/api/auth/upc=52009830171/?format=json

Should return {"gtin_code":"52009830171","gtin_name":"Honey","created":"2016-03-06T04:34:59.001637Z"}
