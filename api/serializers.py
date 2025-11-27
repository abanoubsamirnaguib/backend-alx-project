from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Category, FoodType, Ingredient, Order, OrderItem

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name', 'price', 'image', 'layer_order', 'is_default']

class FoodTypeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True, read_only=True)
    
    class Meta:
        model = FoodType
        fields = ['id', 'name', 'base_price', 'image', 'category', 'ingredients']

class CategorySerializer(serializers.ModelSerializer):
    food_types = FoodTypeSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'image', 'food_types']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
        read_only_fields = ['id']

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'}, label='Confirm Password')
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2', 'first_name', 'last_name']
    
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs
    
    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        return user

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'food_type', 'selected_ingredients', 'ingredients_order']

class OrderItemDetailSerializer(serializers.ModelSerializer):
    food_type = FoodTypeSerializer(read_only=True)
    selected_ingredients = IngredientSerializer(many=True, read_only=True)
    
    class Meta:
        model = OrderItem
        fields = ['id', 'food_type', 'selected_ingredients', 'ingredients_order']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'is_guest', 'customer_name', 'phone_number', 'address', 'notes', 'total_price', 'items', 'created_at']
        read_only_fields = ['user', 'created_at']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        request = self.context.get('request')
        
        # Set user if authenticated
        if request and request.user.is_authenticated:
            validated_data['user'] = request.user
            validated_data['is_guest'] = False
        else:
            validated_data['is_guest'] = True
        
        order = Order.objects.create(**validated_data)
        for item_data in items_data:
            ingredients = item_data.pop('selected_ingredients')
            ingredients_order = item_data.pop('ingredients_order', [])
            order_item = OrderItem.objects.create(order=order, ingredients_order=ingredients_order, **item_data)
            order_item.selected_ingredients.set(ingredients)
        return order

class OrderHistorySerializer(serializers.ModelSerializer):
    items = OrderItemDetailSerializer(many=True, read_only=True)
    
    class Meta:
        model = Order
        fields = ['id', 'customer_name', 'phone_number', 'address', 'notes', 'total_price', 'items', 'created_at']
