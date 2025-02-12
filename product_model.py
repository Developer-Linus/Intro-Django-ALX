from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2)
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Create a Product instance
p = Product(name = "Television", description = "12-Inch smart television", price = 600.12, category = "electronics")
p.save()

# Retrieve
Product.objects.all()

# Update object using ORM
p = Product.objects.get(pk=1)
a.price = 650.50
a.save()

# Delete
a = Product.objects.get(pk=1)
a.delete()

#filter
Product.objects.filter(category = "electronics").order_by(price)

