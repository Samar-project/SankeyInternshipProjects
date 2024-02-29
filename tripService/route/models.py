from django.db import models
from django.core.validators import RegexValidator
from django.forms import ValidationError


class Route(models.Model):
    route_id = models.CharField(primary_key=True,max_length=15,
        validators=[RegexValidator(r'^\d{8,15}$', message="Enter a min 8 digit.")]
    )
    user_id = models.CharField( unique=True,max_length=15)
    route_name = models.CharField(max_length=255)
    route_origin = models.CharField(max_length=255)
    route_destination = models.CharField(max_length=255)
    stops = models.JSONField()
    
    def save(self, *args, **kwargs):
        # Implement custom primary key logic
        if self.route_id:
            self.route_id = 'RT' + str(self.route_id)  # You need to implement get_next_trip_id function
        super(Route, self).save(*args, **kwargs)
        
    def clean(self):
        for stop in self.stops:
            if 'lat' not in stop or 'long' not in stop or 'stopname' not in stop:
                raise ValidationError("Each stop should have 'lat', 'long', and 'stopname'.")