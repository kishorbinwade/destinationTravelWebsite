# Generated by Django 2.2.4 on 2019-09-03 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello11', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]