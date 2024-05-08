
# Vendor Management System Using DJANGO
Develop a vendor management system in Django with REST APIs using Django Rest Framework to showcase vendor performance and track purchase orders, securing every endpoint with JWT token authentication.

## Requirements
- Django (version 4.2.7)
- Python (version 3.10)

## Project Setup


- python -m django startproject project_name
- python manage.py startapp app_name

## Documentation

- After setting up the project, make sure to include the app_name in the INSTALLED_APPS list in the project's settings.py file.
- Then, connect the project's main URLs to the URLs of the app by including the app's URLs in the project's main URLs configuration.





## Database setup

After creating the models in Vendor (Vendor), Purchase_orders (PurchaseOrder), and Performance (VendorPerformance), make sure to register these models in their corresponding admin.py files.

Then run migrations in terminal

- Python manage.py makemigrations
- python manage.py migrate

## Run Server

Run server -  python manage.py runserver
## JWT Authentication

- Implemented JWT Authentication 
To access the token perform http://127.0.0.1:8000/token/. 
- Provide {"username": "siddu11", "password" : "1234"}
- Once you obtain the access token, you can paste it in the Bearer Authentication header and then proceed to implement any API endpoint related to JWT authentication.
## API Endpoints

VENDOR API
- POST    : api/vendors/post/
- GET     : api/vendors/get/
- GET(ID) : api/vendors/get/<int:vendor_id>
- PUT(ID) : api/vendors/put/<int:vendor_id>
- DELETE  : api/vendors/delete/<int:vendor_id>


PURCHASE_ORDER API

- POST    : api/purchase_orders/
- GET     : api/purchase_orders/
- GET(ID) : api/purchase_orders/<int:pk>/
- PUT(ID) : api/purchase_orders/<int:pk>/
- DELETE  : api/purchase_orders/<int:pk>/

VENDOR PERFORMANCE

- GET     : api/vendors/performance/
## Project Setup


- python -m django startproject project_name
- python manage.py startapp app_name

## Running Tests

To run tests, run the following command

```bash
  python manage.py test
```


## Tech Stack

**Python, Django, Django Rest Framework, Sqlite**

## Screenshots

![Screenshot 2024-05-08 165343](https://github.com/gaddesiddu/Vendor-Management-System/assets/98646175/17c4392a-29bc-4a0d-954c-7ddd293aff3f)

![Screenshot 2024-05-08 165415](https://github.com/gaddesiddu/Vendor-Management-System/assets/98646175/eb6a52b2-c259-415f-bfed-e96d78f63f7d)

![Screenshot 2024-05-08 165440](https://github.com/gaddesiddu/Vendor-Management-System/assets/98646175/d2244384-6a7f-4304-9e6b-b53d82ad5a5d)


