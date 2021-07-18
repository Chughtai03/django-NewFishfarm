# Generated by Django 3.2.3 on 2021-06-17 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fishfarm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('cnic', models.CharField(max_length=18)),
                ('s_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='distributorbasicinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('cnic', models.CharField(max_length=18)),
                ('designation', models.CharField(max_length=50)),
                ('s_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='distributorproduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=200)),
                ('other', models.CharField(max_length=500)),
                ('s_date', models.DateField()),
                ('distributor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fishfarm.distributorbasicinfo')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeBasicInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=35)),
                ('father_name', models.CharField(max_length=35)),
                ('date_of_birth', models.DateTimeField()),
                ('sex', models.CharField(max_length=30)),
                ('married', models.CharField(max_length=30)),
                ('cnic', models.CharField(blank=True, max_length=13, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=35)),
                ('password', models.CharField(max_length=35)),
                ('email', models.CharField(max_length=50)),
                ('identification', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Sell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=3, max_digits=8)),
                ('total', models.DecimalField(decimal_places=3, max_digits=8)),
                ('entrytime', models.DateTimeField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fishfarm.customer')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fishfarm.employeebasicinfo')),
            ],
        ),
        migrations.CreateModel(
            name='purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.IntegerField()),
                ('no_of_item', models.IntegerField()),
                ('total_bill', models.IntegerField()),
                ('s_date', models.DateField()),
                ('distributor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fishfarm.distributorbasicinfo')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fishfarm.distributorproduct')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('certification', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=100)),
                ('other', models.CharField(max_length=100)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fishfarm.employeebasicinfo')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeQualification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=100)),
                ('institute', models.CharField(max_length=100)),
                ('years', models.CharField(max_length=100)),
                ('other', models.CharField(max_length=100)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fishfarm.employeebasicinfo')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeContactDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=30)),
                ('addres', models.CharField(max_length=100)),
                ('phone_no', models.CharField(max_length=30)),
                ('phone_no_2', models.CharField(max_length=30)),
                ('landline', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fishfarm.employeebasicinfo')),
            ],
        ),
        migrations.CreateModel(
            name='distributorpayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paid_amount', models.IntegerField()),
                ('remaining_amount', models.IntegerField()),
                ('discount', models.IntegerField()),
                ('payment_method', models.CharField(max_length=50)),
                ('payment_type', models.CharField(max_length=50)),
                ('s_date', models.DateField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fishfarm.distributorproduct')),
            ],
        ),
        migrations.CreateModel(
            name='distributorcontact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('phone', models.IntegerField()),
                ('landline', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('other', models.CharField(max_length=500)),
                ('s_date', models.DateField()),
                ('distributor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fishfarm.distributorbasicinfo')),
            ],
        ),
        migrations.CreateModel(
            name='customercontact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=200)),
                ('s_date', models.DateField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fishfarm.customer')),
            ],
        ),
    ]