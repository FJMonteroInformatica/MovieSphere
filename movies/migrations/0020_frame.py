# Generated by Django 5.0.2 on 2024-05-16 10:59

import django.db.models.deletion
import movies.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0019_movie_budget_currency_movie_revenue_currency_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Frame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.ImageField(upload_to=movies.models.movie_directory_path)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='frames', to='movies.movie')),
            ],
        ),
    ]
