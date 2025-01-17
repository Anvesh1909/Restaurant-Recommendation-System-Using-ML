# Generated by Django 4.2.7 on 2023-11-21 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0011_alter_orderplaced_order_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderplaced',
            name='City',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='orderplaced',
            name='Name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='orderplaced',
            name='Ratings',
            field=models.FloatField(default=0),
        ),
    ]
