from django.contrib import admin
from .models import Category, FoodType, Ingredient, Order, OrderItem

class IngredientInline(admin.TabularInline):
    model = Ingredient
    extra = 1

class FoodTypeAdmin(admin.ModelAdmin):
    inlines = [IngredientInline]
    list_display = ('name', 'category', 'base_price')
    list_filter = ('category',)

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ('get_ordered_ingredients',)
    fields = ('food_type', 'get_ordered_ingredients')
    
    def get_ordered_ingredients(self, obj):
        if obj.pk and obj.ingredients_order:
            # Display ingredients in the order set by user
            ingredient_ids = obj.ingredients_order
            ingredients = obj.selected_ingredients.filter(id__in=ingredient_ids)
            # Create a dict for quick lookup
            ing_dict = {ing.id: ing.name for ing in ingredients}
            # Display in order
            ordered_names = [f"{i+1}. {ing_dict[ing_id]}" for i, ing_id in enumerate(ingredient_ids) if ing_id in ing_dict]
            return " → ".join(ordered_names) if ordered_names else "No ingredients"
        elif obj.pk:
            # Fallback if no order is set
            ingredients = obj.selected_ingredients.all()
            if ingredients:
                return ", ".join([ing.name for ing in ingredients])
            return "No ingredients selected"
        return "-"
    get_ordered_ingredients.short_description = 'Selected Ingredients (In Order)'

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    list_display = ('id', 'customer_name', 'total_price', 'created_at')

admin.site.register(Category)
admin.site.register(FoodType, FoodTypeAdmin)
admin.site.register(Ingredient)
admin.site.register(Order, OrderAdmin)
