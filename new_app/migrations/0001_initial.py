# Generated by Django 5.0.7 on 2024-08-05 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WaterLand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('rides', models.CharField(max_length=20)),
                ('ticket_price', models.IntegerField()),
                ('timing', models.CharField(max_length=20)),
            ],
        ),
    ]
