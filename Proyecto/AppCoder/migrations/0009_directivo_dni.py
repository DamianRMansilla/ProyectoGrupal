# Generated by Django 3.1.2 on 2022-01-24 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0008_alumno_dni'),
    ]

    operations = [
        migrations.AddField(
            model_name='directivo',
            name='dni',
            field=models.IntegerField(null=True),
        ),
    ]