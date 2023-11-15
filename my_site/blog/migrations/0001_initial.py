# Generated by Django 4.2.7 on 2023-11-13 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.CharField(max_length=100)),
                ('recipient', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=100)),
                ('left', models.CharField(max_length=100)),
                ('left_boolean', models.BooleanField(default=False)),
                ('country', models.CharField(max_length=100)),
                ('country_boolean', models.BooleanField(default=False)),
                ('city', models.CharField(max_length=100)),
                ('city_boolean', models.BooleanField(default=False)),
                ('delivered_boolean', models.BooleanField(default=False)),
            ],
        ),
    ]