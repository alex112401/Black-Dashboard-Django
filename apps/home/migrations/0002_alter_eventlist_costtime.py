# Generated by Django 3.2.7 on 2021-10-04 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventlist',
            name='costtime',
            field=models.FloatField(blank=True, null=True),
        ),
    ]