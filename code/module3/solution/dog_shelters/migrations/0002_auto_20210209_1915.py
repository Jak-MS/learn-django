# Generated by Django 3.1.6 on 2021-02-09 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dog_shelters', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='adoption_date',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]
