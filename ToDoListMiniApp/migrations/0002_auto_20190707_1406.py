# Generated by Django 2.1 on 2019-07-07 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDoListMiniApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='creation_date',
            field=models.DateField(default='2019-07-07'),
        ),
    ]