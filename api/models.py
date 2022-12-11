import uuid
from django.db import models

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    userID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    password = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Enrollments(models.Model):
    userID = models.ForeignKey('Subscriber', on_delete=models.CASCADE)
    date = models.DateField()
    month = models.IntegerField()
    year = models.IntegerField()
    batchId = models.ForeignKey('Batch', on_delete=models.CASCADE)
    payment_transaction_id = models.CharField(max_length=255)

    class Meta:
        unique_together = (('userID', 'month', 'year'),)

    def __str__(self):
        return self.payment_transaction_id

class Batch(models.Model):
    batchId = models.IntegerField(primary_key=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    instructor_name = models.CharField(max_length=255)

    def __str__(self):
        return self.instructor_name