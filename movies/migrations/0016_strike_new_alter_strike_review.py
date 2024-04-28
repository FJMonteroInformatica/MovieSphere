# Generated by Django 5.0.2 on 2024-04-28 19:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0015_alter_review_publicationdate'),
        ('news', '0006_alter_new_publicationdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='strike',
            name='new',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='strike', to='news.new'),
        ),
        migrations.AlterField(
            model_name='strike',
            name='review',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='strike', to='movies.review'),
        ),
    ]
