# Generated by Django 3.1.4 on 2021-03-31 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='model',
            field=models.CharField(max_length=100),
        ),
    ]