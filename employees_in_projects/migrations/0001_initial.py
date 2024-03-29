# Generated by Django 4.0.1 on 2022-01-25 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0001_initial'),
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeesInProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days_in_project', models.PositiveIntegerField()),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.employee')),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
            ],
        ),
    ]
