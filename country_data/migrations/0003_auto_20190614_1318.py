# Generated by Django 2.2.2 on 2019-06-14 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('country_data', '0002_auto_20190614_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='population',
            field=models.IntegerField(blank=True),
        ),
    ]