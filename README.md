# FirstPizzaAppMoberries

## overview:

### Requirements:
        ubuntu-16.04
        python 3.4.5
        certifi==2017.1.23
        Django==2.0.9
        django-filter==2.0.0
        djangorestframework==3.9.0
        psycopg2==2.7.6.1
        pytz==2018.7
    
### Installation:
        conda create -n pizzaEnv python 3.4.5 anaconda
        source activate pizzaEnv
        psql\> createdb myprojectuser
        change password accordingly in setting.py file
        inside project folder run below commands
        python manage.py makemigrations
        python manage.py migrate
    
### To Run Project
        #inside project folder run the below command
        python manage.py runserver <port>
    
    
    
    



