# Generated by Django 3.2.18 on 2023-04-01 07:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CompanyApp', '0004_memberinfo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='memberinfo',
            old_name='sliderImg',
            new_name='picture',
        ),
    ]
