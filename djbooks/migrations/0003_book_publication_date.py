# Generated by Django 4.0.5 on 2022-06-20 15:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djbooks', '0002_alter_publisher_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='publication_date',
            field=models.DateField(default=datetime.date(1900, 1, 1)),
        ),
    ]
