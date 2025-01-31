# Generated by Django 5.0.2 on 2025-01-31 16:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('payments', '0001_initial'),
        ('properties', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='lease',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.lease'),
        ),
    ]
