from django.db import models

from positions.models import Position


class Employee(models.Model):
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    position_id = models.ForeignKey(Position, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
