# Generated by Django 3.2.3 on 2021-06-18 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fishfarm', '0002_customer_customercontact_distributorbasicinfo_distributorcontact_distributorpayment_distributorprodu'),
    ]

    operations = [
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=35)),
                ('identification', models.CharField(max_length=10)),
            ],
        ),
    ]