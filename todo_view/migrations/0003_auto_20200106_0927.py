# Generated by Django 2.0.1 on 2020-01-06 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_view', '0002_auto_20200106_0605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateField(),
        ),
    ]