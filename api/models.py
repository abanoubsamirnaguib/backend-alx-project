from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='categories/', blank=True, null=True)

    def __str__(self):
        return self.name

class FoodType(models.Model):
    category = models.ForeignKey(Category, related_name='food_types', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    base_price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='food_types/') # The base image (e.g., empty plate or bottom bun)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    food_type = models.ForeignKey(FoodType, related_name='ingredients', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    image = models.ImageField(upload_to='ingredients/')
    layer_order = models.IntegerField(default=0) # For z-index stacking
    is_default = models.BooleanField(default=False) # If it's a default ingredient like the burger patty

    def __str__(self):
        return f"{self.name} ({self.food_type.name})"

class Order(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')
    is_guest = models.BooleanField(default=False)
    customer_name = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        if self.user:
            return f"Order #{self.id} - {self.user.username}"
        return f"Order #{self.id} - {self.customer_name}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    food_type = models.ForeignKey(FoodType, on_delete=models.CASCADE)
    selected_ingredients = models.ManyToManyField(Ingredient)
    # Store the custom order of ingredients as set by user (list of ingredient IDs)
    ingredients_order = models.JSONField(default=list, blank=True)
    
    def __str__(self):
        return f"{self.food_type.name} for Order #{self.order.id}"
