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
