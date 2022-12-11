from rest_framework import serializers
from datetime import date, datetime
from .models import Subscriber, Enrollments, Batch

class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = ['email', 'userID', 'name', 'phone_number', 'date_of_birth', 'password', 'gender']

    def validate_date_of_birth(self, value):
        # Convert the value to a date object
        date_of_birth = value
        if type(value) == str:
            date_of_birth = datetime.strptime(value, "%Y-%m-%d").date()
        today = date.today()
        age = today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
        if age < 18 or age > 65:
            raise serializers.ValidationError("Age must be between 18 and 65")
        return value

class EnrollmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollments
        fields = '__all__'

class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = '__all__'