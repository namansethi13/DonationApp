# Generated by Django 4.2.1 on 2023-06-24 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetails',
            name='college',
        ),
        migrations.RemoveField(
            model_name='userdetails',
            name='is_college_amabassador',
        ),
        migrations.RemoveField(
            model_name='userdetails',
            name='is_email_verified',
        ),
        migrations.AddField(
            model_name='userdetails',
            name='rating',
            field=models.IntegerField(null=True),
        ),
    ]