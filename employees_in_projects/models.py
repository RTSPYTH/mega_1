from django.db import models

from employees.models import Employee
from projects.models import Project


class EmployeesInProject(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    days_in_project = models.PositiveIntegerField()

    def __str__(self):
        return f'Проект: {self.project_id}, дней в проекте: {self.days_in_project}'
