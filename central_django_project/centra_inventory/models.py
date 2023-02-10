from django.db import models
from django.contrib.auth.models import User

#BaseModel is used to save creation and updation details

class BaseModel(models.Model):
    #auto_now_add adds when created
    #auto_now adds when created or updated
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    #created_by and updated_by alreaady in django backend, we define them here more but functionality done
    #in backend so created_by only called when created and not updated
    #%(class)s is generic term for the classes Sites, Order, IAP and Switch so they will be added when called
    created_by = models.ForeignKey(User, related_name = "%(class)s_createdby", on_delete = models.CASCADE, null = True)
    updated_by = models.ForeignKey(User, related_name = "%(class)s_updatedby", on_delete = models.CASCADE, null = True)

class Site(BaseModel):
    side_id = models.IntegerField(primary_key = True)
    site_name = models.CharField(max_length = 100, null = False, default = '')
    address = models.CharField(max_length = 100, null = False, default = '')
    state = models.CharField(max_length = 100, null = False, default = '')
    country = models.CharField(max_length = 100, null = False, default = '')
    zipcode = models.IntegerField(null = False, default = 0)

    def __str__(self) -> str:
        return self.site_name

class Order(BaseModel):
    # status 2 fields: 0th index what seen in code, 2nd what seen in app. 2nd can be different
    STATUS = (
        ('Pending', 'Pending'),
        ('In-Transit', 'In-Transit'),
        ('Delivered', 'Delivered')
    )
    order_id = models.IntegerField(primary_key = True)
    purchase_id = models.CharField(max_length = 100, null = False, default = '')
    quantity = models.IntegerField(null = False, default = 0)
    type = models.CharField(max_length = 100, null = False, default = '')
    #choices makes it a dropdown. Max_length here restricts length in dropbox
    status = models.CharField(max_length = 100, choices = STATUS, default = '')

    def __str__(self) -> str:
        return str(self.order_id)

class IAP(BaseModel):
    serial_number = models.IntegerField(primary_key = True)
    ip_address = models.CharField(max_length = 100, null = False, default = '')
    mac_address = models.CharField(max_length = 100, null = False, default = '')
    IAP_model = models.CharField(max_length = 100, null = False, default = '')
    IAP_status = models.CharField(max_length = 100, null = False, default = '')
    is_virtual = models.BooleanField(null = False, default = 0)
    #related_name references parent class so no need to join when writing query.
    #on_delete = CASCADE will delete order field if the original field is deleted in the primary key table
    #else it will cause error searching for a deleted field
    IAP_site = models.ForeignKey(Site, related_name = 'iapsite', on_delete = models.CASCADE)
    IAP_order = models.ForeignKey(Order, related_name = 'iaporder', on_delete = models.CASCADE)

    def __str__(self) -> str:
        return str(self.serial_number)
    
class Switch(BaseModel):
    serial_number = models.IntegerField(primary_key = True)
    ip_address = models.CharField(max_length = 100, null = False, default = '')
    mac_address = models.CharField(max_length = 100, null = False, default = '')
    switch_model = models.CharField(max_length = 100, null = False, default = '')
    switch_status = models.CharField(max_length = 20, null = False, default = '')
    switch_site = models.ForeignKey(Site, related_name = 'switchsite', on_delete = models.CASCADE)
    switch_order = models.ForeignKey(Order, related_name = 'switchorder', on_delete = models.CASCADE)

    def __str__(self) -> str:
        return str(self.serial_number)