# Generated by Django 4.2.2 on 2023-12-06 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Age', models.IntegerField()),
                ('Contact', models.IntegerField()),
                ('E_Mail', models.EmailField(max_length=254)),
            ],
        ),
    ]