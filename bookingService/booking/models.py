# booking_project/booking_app/models.py

from django.db import models
from django.core.validators import RegexValidator,EmailValidator
# from trip.models import Trip

class Booking(models.Model):
    ticket_id = models.CharField(primary_key=True, unique=True, validators=[RegexValidator(r'^\d{8,15}$', message="Enter a valid Id.")])
    trip_id = models.CharField(unique=True, max_length=15)
    traveller_name = models.CharField(max_length=255)
    traveller_Phone_no = models.CharField(max_length=15, validators=[RegexValidator(r'^\+?1?\d{9,15}$', message='Enter a valid phone number.')])
    ticket_cost = models.FloatField()
    traveller_email = models.EmailField(validators=[EmailValidator(message="Enter a valid email address.")])
    
    def save(self, *args, **kwargs):
        # Implement custom primary key logic
        if self.ticket_id:
            self.ticket_id = 'TK' + str(self.ticket_id)  
        super(Booking, self).save(*args, **kwargs)
