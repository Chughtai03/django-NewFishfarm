#from web_project.fishfarm.models import contact
from django.contrib import admin
from . models import *
# Register your models here.
class logindata(admin.ModelAdmin):
 list_display=('id', 'username', 'password', 'email', 'identification')
class registerdata(admin.ModelAdmin):
 list_display=('id', 'email', 'password', 'identification')
class customerdata(admin.ModelAdmin):
 list_display=('id', 'name', 'cnic', 's_date')

class customercontactdata(admin.ModelAdmin):
 list_display=('id', 'customer', 'city', 'phone', 'email', 'address', 's_date')

class distributorbasicinfodata(admin.ModelAdmin):
 list_display=('id', 'fname', 'lname', 'cnic', 'designation', 's_date')

class distributorcontactdata(admin.ModelAdmin):
 list_display=('id', 'distributor', 'city', 'address', 'phone', 'landline', 'email', 'other', 's_date')

class distributorproductdata(admin.ModelAdmin):
 list_display=('id', 'distributor', 'company', 'description', 'other', 's_date')

class  purchasedata(admin.ModelAdmin):
 list_display=('id', 'distributor', 'product', 'unit', 'no_of_item', 'total_bill', 's_date')

class distributorpaymentdata(admin.ModelAdmin):
 list_display=('id', 'product', 'paid_amount', 'remaining_amount', 'discount', 'payment_method', 'payment_type', 's_date')

class OrderItemInline(admin.TabularInline):
    model = orderel
    raw_id_fields = ['order']

@admin.register(req)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id']
    #list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]

admin.site.register(login, logindata)
admin.site.register(register,registerdata)
admin.site.register(EmployeeBasicInfo)
admin.site.register(EmployeeContactDetail)
admin.site.register(EmployeeSkill)
admin.site.register(EmployeeQualification)
admin.site.register(Sell)
admin.site.register(customer, customerdata)
admin.site.register(customercontact, customercontactdata)
admin.site.register(distributorbasicinfo, distributorbasicinfodata)
admin.site.register(distributorcontact, distributorcontactdata)
admin.site.register(distributorproduct, distributorproductdata)
admin.site.register( purchase, purchasedata)
admin.site.register(contact)
admin.site.register(distributorpayment, distributorpaymentdata)
admin.site.register(products)
admin.site.register(sproducts)
admin.site.register(team)