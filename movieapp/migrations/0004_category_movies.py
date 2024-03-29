# Generated by Django 4.2.2 on 2023-12-10 06:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Movie_name', models.CharField(max_length=50)),
                ('Movie_image', models.ImageField(default='null.jpg', upload_to='movies')),
                ('Movie_cast', models.CharField(max_length=50)),
                ('Movie_director', models.CharField(max_length=50)),
                ('Movie_trailer', models.URLField()),
                ('Category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='movieapp.category')),
            ],
        ),
    ]
