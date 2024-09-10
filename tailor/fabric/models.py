from django.db import models

class Fabric(models.Model):
    fabric_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price_per_meter = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Design(models.Model):
    design_id = models.AutoField(primary_key=True)
    order = models.ForeignKey('order.Order', on_delete=models.CASCADE)
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    design_name = models.CharField(max_length=255)
    design_image = models.CharField(max_length=255, blank=True, null=True)
    design_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.design_name
