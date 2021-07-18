# Generated by Django 3.2.3 on 2021-07-17 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fishfarm', '0011_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('name', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
    ]
