# Generated by Django 5.0 on 2023-12-28 07:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0007_feedback_reviews'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviews',
            name='user_name',
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
        migrations.DeleteModel(
            name='Reviews',
        ),
    ]
