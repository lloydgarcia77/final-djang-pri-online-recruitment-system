# Generated by Django 2.2.3 on 2019-12-24 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pors_app', '0003_auto_20191210_1741'),
    ]

    operations = [
        migrations.AddField(
            model_name='priapplicantjobhiredinfo',
            name='status',
            field=models.CharField(choices=[('Available', 'Available'), ('Terminated', 'Terminated'), ('6 Months Contract', '6 Months Contract')], default=('Available', 'Available'), max_length=100),
        ),
    ]