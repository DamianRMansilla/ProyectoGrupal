# Generated by Django 3.1.2 on 2022-02-16 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0026_auto_20220216_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', upload_to='avatares'),
        ),
        migrations.DeleteModel(
            name='Avatar',
        ),
    ]
