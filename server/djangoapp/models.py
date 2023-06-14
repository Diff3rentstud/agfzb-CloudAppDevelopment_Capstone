from django.db import models
from django.utils.timezone import now


class CarMake(models.Model):
    name = models.CharField(max_length=10)
    description = models.CharField(max_length=500)
    def __str__(self):
        return f"{self.description}"

class CarModel(models.Model):
    name = models.CharField(max_length=10)
    dealer = models.ForeignKey(CarMake,on_delete=models.CASCADE)
    year = models.DateField(auto_now=True)
    MODEL_CHOICES = [
        ('SEDAN','Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('PICKUP', 'Pickup')
    ]
    type_model = models.CharField(
        null=False,
        max_length=9,
        choices=MODEL_CHOICES,
        default='Sedan'
    )

    def __str__(self):
        return f"{self.dealer + self.name}"

# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
