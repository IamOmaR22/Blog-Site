# Generated by Django 2.2.1 on 2019-07-23 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0007_auto_20190723_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='documents/'),
        ),
    ]
