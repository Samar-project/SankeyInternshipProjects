from django.db import models
from route.models import Route
from django.core.validators import RegexValidator

# from route.models import 


class Trip(models.Model):
    trip_id = models.CharField(primary_key=True,max_length=15
        ,validators=[RegexValidator(r'^\d{8,15}$', message="Accept minimum 8 digit, only Integer.")]
    )
    user_id = models.ForeignKey(Route, to_field='user_id', on_delete=models.CASCADE)
    vehicle_id = models.CharField(max_length=255)  # Assuming Vehicle is a separate model
    route_id = models.ForeignKey(Route, on_delete=models.CASCADE,related_name='trips_as_route')
    driver_name = models.CharField(max_length=255)
    trip_distance = models.FloatField()
    
    
    def save(self, *args, **kwargs):
        # Implement custom primary key logic
        if self.trip_id:
            self.trip_id = 'TP' + str(self.trip_id) 
        super(Trip, self).save(*args, **kwargs)