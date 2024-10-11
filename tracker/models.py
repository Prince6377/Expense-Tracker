from django.db import models
import uuid
# Create your models here.


class Basemodel(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4 , primary_key=True , editable=False , unique=True)
    creted_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)


class Transaction(Basemodel):
    discription = models.CharField(max_length=100)
    ammount = models.FloatField()
    
    def isNegative(self):
        return self.ammount < 0
    
