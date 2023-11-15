from django.db import models

class Post(models.Model):
    order = models.CharField(max_length=100)
    recipient = models.CharField(max_length=100)
    code = models.CharField(max_length=100)

    left = models.CharField(max_length=100)
    left_boolean = models.BooleanField(default=False)

    country = models.CharField(max_length=100)
    country_boolean = models.BooleanField(default=False)

    city = models.CharField(max_length=100)
    city_boolean = models.BooleanField(default=False)

    delivered_boolean = models.BooleanField(default=False)

    def __str__(self):
        return self.recipient