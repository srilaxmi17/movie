# Generated by Django 4.2.2 on 2024-01-08 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0020_payment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='expiry_date',
        ),
    ]