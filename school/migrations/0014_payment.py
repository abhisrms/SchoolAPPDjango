# Generated by Django 5.0.1 on 2024-02-05 05:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0013_alter_fee_amount_alter_fee_cl'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_received', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_received', models.DateField()),
                ('collected_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='school.teacherextra')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.studentextra')),
            ],
        ),
    ]
