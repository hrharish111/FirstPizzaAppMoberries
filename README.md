# FirstPizzaAppMoberries

## overview:
This is interview code test given by moberries,and the tasks was as below
Imagine a pizza ordering services with the following functionality:
1. Order a pizza:
 - There should be a possibility to specify the desired pizzas, the number of pizzas and their size;
 - An order should contain an information regarding the customer;
 - It should be possible to track the status of order delivery.
2. Update an order:
 - There should be a possibility to update the order details (pizzas/number of pizzas/size). Please, pay attention, that order in some delivery statuses (e.g. delivered) could not be updated;
 - There should be a possibility to change the status of order delivery.
3. Remove an order.
4. Retrieve an order:
 - It should be possible to retrieve the order by its identifier.
5. List orders:
 - It should be possible to retrieve all the orders;
 - Some filtering by status/customers will be nice to have.

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
    
    
    
    



