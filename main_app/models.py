from django.db import models
from django.urls import reverse

WATERS = (
    ('W', 'Watered'),
    ('N', 'Not Watered')
)

# Create your models here.

class Plant(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=250)


    def __str__(self):
        return f'{self.name} ({self.id})'

    def get_absolute_url(self):
            return reverse('detail', kwargs={'plant_id': self.id})


class Feeding(models.Model):
    date = models.DateField('feeding date')
    water = models.CharField(
        max_length=1,
        choices=WATERS,
	    default=WATERS[0][0]
    )
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.get_water_display()} on {self.date}"

    class Meta:
        ordering = ['-date']