# Generated by Django 4.2.5 on 2023-10-03 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Average',
            field=models.FloatField(default=False),
        ),
    ]