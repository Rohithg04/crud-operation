from django.db import models

#Create your models here

class WaterLand(models.Model):
    age_category = (
        ('child','child'),
        ('adult','adult')
    )

    name=models.CharField(max_length=20)
    age=models.IntegerField()
    rides_name=models.CharField(max_length=20)
    ticket_price=models.IntegerField()
    timing=models.CharField(max_length=20)
    category=models.CharField(max_length=20,choices=age_category)