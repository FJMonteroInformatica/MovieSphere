# Generated by Django 5.0.2 on 2024-05-16 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0021_performance_screentime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='performance',
            name='screenTime',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.DeleteModel(
            name='Frame',
        ),
    ]