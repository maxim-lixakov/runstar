How to deploy project locally

1. restore .sql dump of database to local 

you need to install MySql server locally and then create a database "probegorg" and source ".sql" file to restore 
database locally

2. create models in django by existing database

you need to create a new empty django project locally and then run "python manage.py inspectdb" to create models
or restored database

3. integrate Wagtail cms into our project

to integrate wagtail to existing project you need to follow the documentation - 
https://docs.wagtail.org/en/stable/getting_started/integrating_into_django.html
