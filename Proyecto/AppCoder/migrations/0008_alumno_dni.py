# Generated by Django 3.1.2 on 2022-01-23 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0007_auto_20220123_1009'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='dni',
            field=models.IntegerField(null=True),
        ),
    ]
