# Generated by Django 5.0.1 on 2024-02-11 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0016_payment_remaining_fee'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentextra',
            name='carryover_balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='studentextra',
            name='total_due',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
