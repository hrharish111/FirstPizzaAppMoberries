# Generated by Django 2.0.9 on 2018-12-16 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]