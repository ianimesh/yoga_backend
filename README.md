## Hosted backend details

Backend hosted URL: https://yogabackend-production.up.railway.app/admin/login/?next=/admin/

Backend admin credentials- 

username - admin@yoga

password - 1234


# Django Project
This project is a Django app that uses a SQLite database to store and manage information about Subscribers, Enrollments, and Batches.

Database Structure
The app uses the following models to define the structure of the SQLite database:

Subscriber
The Subscriber model represents a single subscriber to the app. It has the following attributes:

email: The subscriber's email address.
userID: A unique ID automatically generated for the subscriber.
name: The subscriber's name.
phone_number: The subscriber's phone number.
date_of_birth: The subscriber's date of birth.
password: The password for the subscriber's account.
gender: The subscriber's gender.


Enrollment
The Enrollment model represents a single enrollment of a subscriber in a batch. It has the following attributes:

userID: The ID of the subscriber who is enrolled in the batch.
date: The date of the enrollment.
month: The month of the enrollment.
year: The year of the enrollment.
batchId: The ID of the batch in which the subscriber is enrolled.
payment_transaction_id: The ID of the payment transaction for the enrollment.


Batch
The Batch model represents a single batch of classes offered by the app. It has the following attributes:

batchId: HardCoded for the Yoga Class Batches.
start_time: The start time of the batch.
end_time: The end time of the batch.
instructor_name: The name of the instructor for the batch.


Usage
To use the app, you will need to install the following dependencies:

Django: The web framework used to build the app.
djangorestframework: The REST framework used to create the API for the app.
You can install these dependencies using the following commands:


pip install Django
pip install djangorestframework
Once the dependencies are installed, you can run the app using the following command:


python manage.py runserver
This will start the Django development server and make the app available at http://127.0.0.1:8000/.

To access the app's API, you can use the following endpoints:

/subscribers/: This endpoint allows you to create, retrieve, update, and delete Subscriber objects.
/enrollments/: This endpoint allows you to create, retrieve, and delete Enrollment objects.
/batches/: This endpoint allows you to create, retrieve, update, and delete Batch objects.
/login/: This endpoint allows you to authenticate a Subscriber by providing their email address and password.
