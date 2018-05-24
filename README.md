# PizzaOrdersApi
Simple Django Service for Pizza Orders
-----
This app uses Django Rest Framework, so users can:
* See list orders
* Add/update/delete order
* Run test to check app's work (**using pytest**)
## Installation
1. Install python3.6 using offical notes https://www.python.org/downloads/
2. Install virualenv using offical notes https://virtualenv.pypa.io/en/stable/installation/
3. Create and activate new virualenv. See official notes for detail https://virtualenv.pypa.io/en/stable/userguide/
4. Clone repository
5. Go to folder **PizzaOrder** where is file **manage.py**
6. Run command 
    > pip install -r requirements.txt
7. Install PostgreSQL, see official guide to detail https://www.postgresql.org/download/
8. You can create user and database, that specified in **settings.py** with this commands
    > sudo -u postgres createuser pizza_user

    > sudo -u postgres createdb pizza_db

    > sudo -u postgres psql

    > alter user pizza_user with encrypted password 'pizza_pass';

    > grant all privileges on database pizza_db to pizza_user ;

    **P.S. If you want, you can specified our own user and db, but don't forget then edit settings.py**
9. Run command terminal in your vitrualenv, go to folder **PizzaOrder** where is file **manage.py** and run this commands
    > python manage.py makemigrations

    > python manage.py migrate
10. Now you can run app
    > python manage.py runserver
11. Visit http://127.0.0.1:8000/api/ to check work
12. You also can run test using this command:
    > pytest
## How to use
1. Run app
    > python manage.py runserver
2. Go to **http://127.0.0.1:8000/api/** in your browser

    Now you can see UI that provides Django Rest Framework. 
    Here you can see list of pizza orders and form that helps
    to create new order. If you want to get just json data - you 
    need to go **http://127.0.0.1:8000/api/?format=json**
   
3. Go to **http://127.0.0.1:8000/api/uuid/**, set uuid for order that you need.
It can look likes http://127.0.0.1:8000/api/426bb335-71a3-43b9-ab4d-e4cdfd72d54a/
 
    Here you can see UI that provides Django Rest Framework.
    Here you can update/delete pizza order. Also you can just make put/delete requests to http://127.0.0.1:8000/api/uuid/
    withour using any form.

## Expamples working
![Pizza Orders list](https://drive.google.com/uc?export=view&id=18ETGqKPca8g30jE0ZBGu2Sqrsx-aUApV)

![Pizza Order update/delete](https://drive.google.com/uc?export=view&id=1-eE4RuMY1EYnp6nZxpUmzlmRyY8I2oIg)