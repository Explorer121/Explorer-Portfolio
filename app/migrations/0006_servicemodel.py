# Generated by Django 4.0.5 on 2022-08-07 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_homemodel_email_homemodel_location_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=500)),
            ],
        ),
    ]