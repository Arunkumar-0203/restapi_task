# Generated by Django 4.0.3 on 2022-03-30 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi_app', '0003_alter_user_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='DOB',
            field=models.DateField(null=True),
        ),
    ]