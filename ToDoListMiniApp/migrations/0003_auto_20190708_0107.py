# Generated by Django 2.1 on 2019-07-08 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDoListMiniApp', '0002_auto_20190707_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='creation_date',
            field=models.DateField(default='2019-07-08'),
        ),
    ]
