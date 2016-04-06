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

`pip install -r requirements/development.txt`

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

No tokens or keys required for this version of the API, but unless you are logged in, it's read only.

#### Listview of all UPCs in DB so far
https://cafbsite.herokuapp.com/api/v1/

#### Query Products UPCs already in the DB
http://localhost:8000/api/v1/products/857063002645/

Should return {"gtin_code":"857063002645","gtin_name":"Korean Stir Fry","created":"2016-04-06T03:45:13.816144Z"}
