# Generated by Django 3.1.4 on 2021-03-31 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0002_auto_20210331_2134'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
