from django.db import models

# Create your models here.
class login(models.Model):
    username = models.CharField(max_length=35)
    password = models.CharField(max_length=35)
    email = models.CharField(max_length=50)
    identification = models.CharField(max_length=10)
    def _str_(self):
      return str(self.username)
class register(models.Model):
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=35)
    identification = models.CharField(max_length=10)
    def _str_(self):
      return str(self.email)
class EmployeeBasicInfo(models.Model):
    names  = models.CharField(max_length=30) 
    last_name  = models.CharField(max_length=35)
    father_name  = models.CharField(max_length=35)
    date_of_birth = models.DateTimeField()
    sex = models.CharField(max_length=30) 
    married = models.CharField(max_length=30) 
    cnic = models.CharField(max_length=13,unique=True,blank=True)
    def _str_(self):
      return str(self.names)

class  EmployeeContactDetail(models.Model):
    employee=models.ForeignKey(EmployeeBasicInfo,on_delete=models.CASCADE)
    city = models.CharField(max_length=30)
    addres = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=30)
    phone_no_2 = models.CharField(max_length=30)
    landline = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    def __str__(self):
        return self.employee

class EmployeeSkill(models.Model):
    employee=models.ForeignKey(EmployeeBasicInfo,on_delete=models.CASCADE)
    skill = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    certification = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    other = models.CharField(max_length=100)    
    def __str__(self):
        return self.employee

class EmployeeQualification(models.Model):

    employee=models.ForeignKey(EmployeeBasicInfo,on_delete=models.CASCADE)
    degree = models.CharField(max_length=100)
    institute = models.CharField(max_length=100)
    years = models.CharField(max_length=100)
    other = models.CharField(max_length=100)
    def __str__(self):
        return self.employee

class customer(models.Model):
    name=models.CharField(max_length=50)
    cnic=models.CharField(max_length=18)
    s_date=models.DateField()

    def __str__(self):
        return self.name
class customercontact(models.Model):
    
    customer = models.ForeignKey(customer,on_delete=models.CASCADE)
    city=models.CharField(max_length=50)
    phone=models.IntegerField()
    email=models.EmailField()
    address=models.CharField(max_length=200)
    s_date=models.DateField()
    
    def __str__(self):
        return self.customer


class Sell(models.Model):

    customer=models.ForeignKey(customer,on_delete=models.CASCADE)
    employee=models.ForeignKey(EmployeeBasicInfo,on_delete=models.CASCADE)
    quantity = models.IntegerField() 
    price = models.DecimalField(max_digits=8, decimal_places=3)
    total = models.DecimalField(max_digits=8, decimal_places=3)
    entrytime = models.DateTimeField()

class distributorbasicinfo(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    cnic=models.CharField(max_length=18)
    designation=models.CharField(max_length=50)
    s_date=models.DateField()
    
    def __str__(self):
        return self.fname

class distributorcontact(models.Model):
    distributor = models.ForeignKey(distributorbasicinfo,on_delete=models.CASCADE)
    city=models.CharField(max_length=50)
    address=models.CharField(max_length=200)
    phone=models.IntegerField()
    landline=models.IntegerField()
    email=models.EmailField()
    other=models.CharField(max_length=500)
    s_date=models.DateField()
    def __str__(self):
        return self.city

class distributorproduct(models.Model):
   distributor = models.ForeignKey(distributorbasicinfo,on_delete=models.CASCADE)
   company=models.CharField(max_length=500)
   description=models.CharField(max_length=200)
   other=models.CharField(max_length=500)
   s_date=models.DateField()
   def __str__(self):
        return self.company

class purchase(models.Model):
    distributor = models.ForeignKey(distributorbasicinfo,on_delete=models.CASCADE)
    product= models.ForeignKey(distributorproduct,on_delete=models.CASCADE)
    unit=models.IntegerField()
    no_of_item=models.IntegerField()
    total_bill=models.IntegerField()
    s_date=models.DateField()
    
    def __str__(self):
        return self.unit

class distributorpayment(models.Model):
    product= models.ForeignKey(distributorproduct,on_delete=models.CASCADE)
    paid_amount=models.IntegerField()
    remaining_amount=models.IntegerField()
    discount=models.IntegerField()
    payment_method=models.CharField(max_length=50)
    payment_type=models.CharField(max_length=50)
    s_date=models.DateField()
    
    def __str__(self):
        return self.discount

class products(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=100) 
    price = models.FloatField()
    description = models.CharField(max_length=500) 
    def __str__(self):
        return self.name
class sproducts(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=100) 
    price = models.FloatField()
    description = models.CharField(max_length=500) 
    def __str__(self):
        return self.name
class req(models.Model):
    status=models.CharField(max_length=255, default='Pending')
class orderel(models.Model):
    order = models.ForeignKey(req, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    quan= models.FloatField()

    def _str_(self):
        return str(self.order)

class contact(models.Model):
    name = models.CharField(max_length=60) 
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message=models.CharField(max_length=500)
    entrytime = models.DateTimeField()
    def _str_(self):
        return str(self.email)
class team(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=100) 
    status = models.CharField(max_length=100)
    description = models.CharField(max_length=500) 
    def __str__(self):
        return self.name
        