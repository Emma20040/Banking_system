from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=200, null=False)
    age = models.IntegerField(blank=True, null= True)
    country= models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null= True)
    phone = models.IntegerField(blank=True,  null= True)
    balance = models.DecimalField(max_digits=200, decimal_places=3)

    
class Account(models.Model):
    account_num =models.IntegerField(primary_key=True, null= False)
    account_holder= models.ForeignKey(Customer, on_delete=models.CASCADE , null=True)
    balance = models.DecimalField(decimal_places=3, max_digits=30, default=0, null= False)

    def __str__(self):
        return str(self.account_num)
    
    def credit(self, amount):
        try:
            self.balance = self.balance + int(amount)
            self.save()
        except:
            raise ValueError("you don't have enough money to carry out this transaction")
        
    def debit(self, amount):
        try:
            if amoumt<=0:
                raise ValueError("input a valid amount to perform this transaction")
            if amount >= self.balance:
                raise ValueError("insufficint funds")
            
            self.balance = self.balance - int(amount)
            self.save()
        except:
            raise ValueError("Transaction failed")