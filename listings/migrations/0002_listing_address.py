# Generated by Django 3.0.1 on 2020-01-01 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='address',
            field=models.CharField(default=True, max_length=250),
        ),
    ]
