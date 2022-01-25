from django.db import models

from employees.models import Employee


class Salary(models.Model):
    employee_id = models.OneToOneField(Employee, on_delete=models.CASCADE, primary_key=True)
    amount = models.DecimalField(max_digits=10, decimal_places=8)

    def __str__(self):
        return f'{self.amount} $ - {self.employee_id}'
