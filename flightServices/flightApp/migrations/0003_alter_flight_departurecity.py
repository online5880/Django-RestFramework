# Generated by Django 5.1.3 on 2024-11-13 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flightApp', '0002_alter_reservation_flight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='departureCity',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]