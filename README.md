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
        
### List of avaliable API and its info

#### To get list of pizza names avaliable
    GET - http://localhost:8000/api/pizza
    
    Example :-
        response:
            [{
                "id":1,
                "name":"firstpizza"
            },
            {
                "id":2,
                "name":"secondpizza"
            }
            ]
    
#### To create new pizza and to store in db          
    POST -http://localhost:8000/api/pizza
            Example body :-
            {
                "name":"<your_pizza_name>"
            }
          
#### To update or delete particular pizza
    
    PUT -http://localhost:8000/api/pizza/<id>
        Example body
        {
            "name":"<change_name>"
        }
        
    DELETE -http//localhost:8000/api/pizza/<id>
    Example body
    {
    }
    
#### To create sizes for pizza

    PUT - http://localhost:8000/api/pizza_size
    Example body
    {
        "size":"<mention all avaliable sizes>"
    }
    
#### TO get all avaliable sizes
    GET -http://localhost:8000/api/pizza_size
    Example response
    [
    {"id":1,
    "size":10
    },{
    "id":2,
    "size":20
    }]
    
#### To update or delete sizes
    PUT -http://localhost:8000/api/pizza_size/1
    Example body
    {
        "size":"<mention_updated_size>"
    }
    
    DELETE -http://localhost:8000/api/pizza_size/1
    Example body
    {}
    
#### To create new pizza varity and store in db
    POST -http://localhost:8000/api/pizza_varity
    Example body:-
    {
        "pizza":"<mention_pizza_name>",
        "size": "<mention_pizza_size>",
        "price": "<add price for pizza>"
    }
    
#### To get all pizza varity 
    GET - http://localhost:8000/api/pizza_varity
    
    Example response :-
    [
    {
    "id":1,
    "pizza":<pizza_id_will_be_displayed>,
    "size":"<size>",
    "price":"<price>"
    },{
    "id":2,
    "pizza":<pizza_id_will_be_displayed>,
    "size":"<size>",
    "price":"<price>"
    } 
    ]
    
#### To update or delete pizza varity
    PUT -http://localhost:8000/api/pizza_varity/<id>
    Example body:
     {
        "pizza":"<mention_pizza_name>",
        "size": "<mention_pizza_size>",
        "price": "<add price for pizza>"
    }
    
    DELETE -http://localhost:8000/api/pizza_varity/<id>
    
#### To add pizza as items to your order
    POST - http://localhost:8000/api/order_items/
    Example body
    {
    "customer_name": "",
    "customer_address": "",
    "pizza": null,
    "size": null,
    "quantity": null
    }
    
#### To view particular item or all item in the order
    GET - http://localhost:8000/api/order_items/
    Example response
    [
    {
        "id": 1,
        "order": 1,
        "customer_name": "Harish",
        "customer_address": "Test",
        "pizza": 1,
        "size": 2,
        "quantity": 2,
        "price": "200.00"
    },
    {
        "id": 2,
        "order": 1,
        "customer_name": "Harish",
        "customer_address": "Test",
        "pizza": 1,
        "size": 2,
        "quantity": 2,
        "price": "200.00"
    }
    ]
    
    GET -http://localhost:8000/api/order_items/1
    Example response
    {
    "id": 1,
    "order": 1,
    "customer_name": "Harish",
    "customer_address": "Test",
    "pizza": 1,
    "size": 2,
    "quantity": 2,
    "price": "200.00"
    }
    
    
#### To update or delete items that are ordered
    PUT -http://localhost:8000/api/order_items/1/
    Example body
    {
    "id": 1,
    "order": 1,
    "customer_name": "Harish",
    "customer_address": "Test",
    "pizza": 1,
    "size": 2,
    "quantity": 2,
    "price": "200.00"
    }
    
    DELETE-http://localhost:8000/api/order_items/1/
    Example body
    {}
    
#### To view orders all orders, filter by customer name,filter by status and filter by both
    GET -http://localhost:8000/api/orders/
    Example response:
    [
    {
        "id": 1,
        "status": "cancelled",
        "customer_name": "Harish",
        "customer_address": "Test",
        "total": "0.00",
        "items": [
            {
                "id": 1,
                "order": 1,
                "customer_name": "Harish",
                "customer_address": "Test",
                "pizza": 1,
                "size": 2,
                "quantity": 2,
                "price": "200.00"
            },
            {
                "id": 2,
                "order": 1,
                "customer_name": "Harish",
                "customer_address": "Test",
                "pizza": 1,
                "size": 2,
                "quantity": 2,
                "price": "200.00"
            }
        ]
    }
    ]    
    
    GET - http://localhost:8000/api/orders/?status=cancelled
    
    Response will be as above
    
    GET- http://localhost:8000/api/orders/?customer_name=Harish
    
    Response will be as above
    
    GET- http://localhost:8000/api/orders/?customer_name=Harish&status=cancelled
    
    Response will be as above
    
#### To update or delete order

    PUT - http://localhost:8000/api/orders/1
    Example body
    {
    "id": 1,
    "status": "cancelled",
    "customer_name": "Harish",
    "customer_address": "Test",
    "total": "0.00",
    "items": [
        {
            "id": 1,
            "order": 1,
            "customer_name": "Harish",
            "customer_address": "Test",
            "pizza": 1,
            "size": 2,
            "quantity": 2,
            "price": "200.00"
        },
        {
            "id": 2,
            "order": 1,
            "customer_name": "Harish",
            "customer_address": "Test",
            "pizza": 1,
            "size": 2,
            "quantity": 2,
            "price": "200.00"
        }
    ]
    }
    
    Delete -http://localhost:8000/api/orders/1/
    Example body
    {}
    



