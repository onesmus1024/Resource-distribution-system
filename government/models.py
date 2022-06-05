
from django.db import models
import datetime


class Supplier(models.Model):
    """self refers to the current instance of the class"""
    name = models.CharField(max_length=100)
    email = models.EmailField()
    amount_bought = models.IntegerField(default=0)
    product_name = models.CharField(max_length=100,)
    remaining_amount = models.IntegerField(blank=True, null=True,default=0)
    amount_supplied = models.IntegerField(blank=True, null=True,default=0)
    """returns the name of the supplier as the name of the object"""
    def __str__(self):
        return self.name
        
        """metadata of the class that implies this class should be inherited by other classes"""
    class Meta:
        abstract=True

"""inherit from the supplier class"""
class Importer(Supplier):
    imported_from = models.CharField(max_length=100)
    date_of_import = models.DateField(auto_now_add=True,null=True)

    """"function to check if the supplier can import"""
    def can_import(self):
        if self.remaining_amount <=100:
            return True
        else:
            return False
    """return true if importer can supply to local supplier"""
    def can_supply_to_local_supplier(self):
        if self.remaining_amount >= int(self.amount_supplied):
            return True
        else:
            return False
    """reduce the amount remaining by the amount bought"""
    def sell_to_local_supplier(self):
        self.remaining_amount = int(self.remaining_amount) - int(self.amount_supplied)
        self.save()

    """imports the prodcuts from the supplier"""
    def imports(self):
        self.remaining_amount = int(self.remaining_amount) + int(self.amount_bought)
        self.save()
        

class LocalSupplier(Supplier):
    location = models.CharField(max_length=100)
    date_of_delivery = models.DateField(auto_now_add=True,null=True)
    importer = models.ForeignKey(Importer, on_delete=models.CASCADE)
    date_of_purchase = models.DateField(auto_now_add=True,null=True)

    def can_buy_from_importer(self):
        if self.amount_supplied == self.amount_bought:
            return True
        else:
            return False

    def buy_from_impoter(self):
        self.remaining_amount = self.remaining_amount + self.amount_bought
        self.save()

    def sell_to_consumer(self):
        self.remaining_amount -=  int(self.amount_supplied)
        self.save()
    def can_purchase(self):
        if self.remaining_amount <=100:
            return True
        else:
            return False
    def can_sell(self):
        if self.remaining_amount >= int(self.amount_supplied):
            return True
        else:
            return False
class Consumer(models.Model):
     name = models.CharField(max_length=100)
     product_name = models.CharField(max_length=100,default='product')
     LocalSupplier = models.ForeignKey(LocalSupplier,on_delete=models.CASCADE)
     amount_bought = models.IntegerField()
     date_of_purchase = models.DateField(auto_now_add=True,null=True)

     def __str__(self):
        return self.name


class License(models.Model):
    name = models.CharField(max_length=100)
    license_due_date = models.DateField()
    license_date_of_issue = models.DateField()
    expiry_date = models.DateField()


    class Meta:
        abstract=True
    
class ImporterLcence(License):
    importer = models.ForeignKey(Importer, on_delete=models.CASCADE)

    def isValid(self):
        return self.expiry_date<=datetime.date.today()


class LocalSupplierLicense(License):
    local_supplier = models.ForeignKey(LocalSupplier, on_delete=models.CASCADE)

    def isValid(self):
        return self.expiry_date>=datetime.date.today()




    
