from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from api.models import Category, FoodType, Ingredient
import requests
from io import BytesIO

class Command(BaseCommand):
    help = 'Seeds the database with sample food data'

    def download_image(self, url, filename):
        """Download image from URL and return ContentFile"""
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                return ContentFile(response.content, name=filename)
        except Exception as e:
            self.stdout.write(self.style.WARNING(f'Failed to download {filename}: {e}'))
        return None

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding database...')
        
        # Clear existing data
        Ingredient.objects.all().delete()
        FoodType.objects.all().delete()
        Category.objects.all().delete()
        
        # Create Categories with images
        savory = Category.objects.create(name='Savory')
        savory_img = self.download_image('https://images.unsplash.com/photo-1513104890138-7c749659a591?w=400&h=400&fit=crop', 'savory.jpg')
        if savory_img:
            savory.image.save('savory.jpg', savory_img, save=True)
        
        sweets = Category.objects.create(name='Sweets')
        sweets_img = self.download_image('https://images.unsplash.com/photo-1563805042-7684c019e1cb?w=400&h=400&fit=crop', 'sweets.jpg')
        if sweets_img:
            sweets.image.save('sweets.jpg', sweets_img, save=True)
        
        self.stdout.write(self.style.SUCCESS('Created categories'))
        
        # Create Burger Food Type
        burger = FoodType.objects.create(
            category=savory,
            name='Classic Burger',
            base_price=5.99
        )
        burger_img = self.download_image('https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=400&h=400&fit=crop', 'burger_base.jpg')
        if burger_img:
            burger.image.save('burger_base.jpg', burger_img, save=True)
        
        # Create Burger Ingredients
        burger_bun = Ingredient.objects.create(
            food_type=burger,
            name='Burger Bun',
            price=0.00,
            layer_order=1,
            is_default=True
        )
        bun_img = self.download_image('https://images.unsplash.com/photo-1586190848861-99aa4a171e90?w=400&h=400&fit=crop', 'burger_bun.jpg')
        if bun_img:
            burger_bun.image.save('burger_bun.jpg', bun_img, save=True)
        
        burger_patty = Ingredient.objects.create(
            food_type=burger,
            name='Beef Patty',
            price=0.00,
            layer_order=2,
            is_default=True
        )
        patty_img = self.download_image('https://images.unsplash.com/photo-1607013251379-e6eecfffe234?w=400&h=400&fit=crop', 'burger_patty.jpg')
        if patty_img:
            burger_patty.image.save('burger_patty.jpg', patty_img, save=True)
        
        lettuce = Ingredient.objects.create(
            food_type=burger,
            name='Lettuce',
            price=0.50,
            layer_order=3,
            is_default=False
        )
        lettuce_img = self.download_image('https://images.unsplash.com/photo-1622206151226-18ca2c9ab4a1?w=400&h=400&fit=crop', 'lettuce.jpg')
        if lettuce_img:
            lettuce.image.save('lettuce.jpg', lettuce_img, save=True)
        
        tomato = Ingredient.objects.create(
            food_type=burger,
            name='Tomato',
            price=0.50,
            layer_order=4,
            is_default=False
        )
        tomato_img = self.download_image('https://images.unsplash.com/photo-1546094096-0df4bcaaa337?w=400&h=400&fit=crop', 'tomato.jpg')
        if tomato_img:
            tomato.image.save('tomato.jpg', tomato_img, save=True)
        
        cheese = Ingredient.objects.create(
            food_type=burger,
            name='Cheese',
            price=1.00,
            layer_order=5,
            is_default=False
        )
        cheese_img = self.download_image('https://images.unsplash.com/photo-1618164436241-4473940d1f5c?w=400&h=400&fit=crop', 'cheese.jpg')
        if cheese_img:
            cheese.image.save('cheese.jpg', cheese_img, save=True)
        
        onion = Ingredient.objects.create(
            food_type=burger,
            name='Onion Rings',
            price=1.50,
            layer_order=6,
            is_default=False
        )
        onion_img = self.download_image('https://images.unsplash.com/photo-1639024471283-03518883512d?w=400&h=400&fit=crop', 'onion_rings.jpg')
        if onion_img:
            onion.image.save('onion_rings.jpg', onion_img, save=True)
        
        bacon = Ingredient.objects.create(
            food_type=burger,
            name='Bacon',
            price=2.00,
            layer_order=7,
            is_default=False
        )
        bacon_img = self.download_image('https://images.unsplash.com/photo-1528607929212-2636ec44253e?w=400&h=400&fit=crop', 'bacon.jpg')
        if bacon_img:
            bacon.image.save('bacon.jpg', bacon_img, save=True)
        
        self.stdout.write(self.style.SUCCESS('Created Burger with ingredients'))
        
        # Create Pizza Food Type
        pizza = FoodType.objects.create(
            category=savory,
            name='Custom Pizza',
            base_price=8.99
        )
        pizza_img = self.download_image('https://images.unsplash.com/photo-1513104890138-7c749659a591?w=400&h=400&fit=crop', 'pizza_base.jpg')
        if pizza_img:
            pizza.image.save('pizza_base.jpg', pizza_img, save=True)
        
        # Pizza Ingredients
        pizza_dough = Ingredient.objects.create(
            food_type=pizza,
            name='Pizza Dough & Sauce',
            price=0.00,
            layer_order=1,
            is_default=True
        )
        dough_img = self.download_image('https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=400&h=400&fit=crop', 'pizza_dough.jpg')
        if dough_img:
            pizza_dough.image.save('pizza_dough.jpg', dough_img, save=True)
        
        mozzarella = Ingredient.objects.create(
            food_type=pizza,
            name='Mozzarella Cheese',
            price=0.00,
            layer_order=2,
            is_default=True
        )
        mozz_img = self.download_image('https://images.unsplash.com/photo-1618164436241-4473940d1f5c?w=400&h=400&fit=crop', 'mozzarella.jpg')
        if mozz_img:
            mozzarella.image.save('mozzarella.jpg', mozz_img, save=True)
        
        pepperoni = Ingredient.objects.create(
            food_type=pizza,
            name='Pepperoni',
            price=1.50,
            layer_order=3,
            is_default=False
        )
        pep_img = self.download_image('https://images.unsplash.com/photo-1628840042765-356cda07504e?w=400&h=400&fit=crop', 'pepperoni.jpg')
        if pep_img:
            pepperoni.image.save('pepperoni.jpg', pep_img, save=True)
        
        mushrooms = Ingredient.objects.create(
            food_type=pizza,
            name='Mushrooms',
            price=1.00,
            layer_order=4,
            is_default=False
        )
        mush_img = self.download_image('https://images.unsplash.com/photo-1516714435131-44d6b64dc6a2?w=400&h=400&fit=crop', 'mushrooms.jpg')
        if mush_img:
            mushrooms.image.save('mushrooms.jpg', mush_img, save=True)
        
        olives = Ingredient.objects.create(
            food_type=pizza,
            name='Black Olives',
            price=0.75,
            layer_order=5,
            is_default=False
        )
        olives_img = self.download_image('https://res.cloudinary.com/perkchops/image/upload/c_scale,w_350/v1600257706/ingredients/2020816151/cuzi253qnuo5ttjmouny.jpg', 'olives.jpg')
        if olives_img:
            olives.image.save('olives.jpg', olives_img, save=True)
        
        bell_peppers = Ingredient.objects.create(
            food_type=pizza,
            name='Bell Peppers',
            price=0.75,
            layer_order=6,
            is_default=False
        )
        peppers_img = self.download_image('https://images.unsplash.com/photo-1563565375-f3fdfdbefa83?w=400&h=400&fit=crop', 'bell_peppers.jpg')
        if peppers_img:
            bell_peppers.image.save('bell_peppers.jpg', peppers_img, save=True)
        
        self.stdout.write(self.style.SUCCESS('Created Pizza with ingredients'))
        
        # Create Sandwich Food Type
        sandwich = FoodType.objects.create(
            category=savory,
            name='Deli Sandwich',
            base_price=4.99
        )
        sandwich_img = self.download_image('https://images.unsplash.com/photo-1509722747041-616f39b57569?w=400&h=400&fit=crop', 'sandwich_base.jpg')
        if sandwich_img:
            sandwich.image.save('sandwich_base.jpg', sandwich_img, save=True)
        
        # Sandwich Ingredients
        bread = Ingredient.objects.create(
            food_type=sandwich,
            name='Bread',
            price=0.00,
            layer_order=1,
            is_default=True
        )
        bread_img = self.download_image('https://images.unsplash.com/photo-1509440159596-0249088772ff?w=400&h=400&fit=crop', 'bread.jpg')
        if bread_img:
            bread.image.save('bread.jpg', bread_img, save=True)
        
        turkey = Ingredient.objects.create(
            food_type=sandwich,
            name='Turkey',
            price=2.00,
            layer_order=2,
            is_default=False
        )
        turkey_img = self.download_image('https://images.unsplash.com/photo-1587593810167-a84920ea0781?w=400&h=400&fit=crop', 'turkey.jpg')
        if turkey_img:
            turkey.image.save('turkey.jpg', turkey_img, save=True)
        
        ham = Ingredient.objects.create(
            food_type=sandwich,
            name='Ham',
            price=2.00,
            layer_order=3,
            is_default=False
        )
        ham_img = self.download_image('https://www.farmfreshxpress.com/cdn/shop/products/HamSlicesStock_1_493x.jpg?v=1655843535', 'ham.jpg')
        if ham_img:
            ham.image.save('ham.jpg', ham_img, save=True)
        
        swiss_cheese = Ingredient.objects.create(
            food_type=sandwich,
            name='Swiss Cheese',
            price=1.00,
            layer_order=4,
            is_default=False
        )
        swiss_img = self.download_image('https://images.unsplash.com/photo-1618164436241-4473940d1f5c?w=400&h=400&fit=crop', 'swiss_cheese.jpg')
        if swiss_img:
            swiss_cheese.image.save('swiss_cheese.jpg', swiss_img, save=True)
        
        sandwich_lettuce = Ingredient.objects.create(
            food_type=sandwich,
            name='Lettuce',
            price=0.50,
            layer_order=5,
            is_default=False
        )
        slettuce_img = self.download_image('https://images.unsplash.com/photo-1622206151226-18ca2c9ab4a1?w=400&h=400&fit=crop', 'sandwich_lettuce.jpg')
        if slettuce_img:
            sandwich_lettuce.image.save('sandwich_lettuce.jpg', slettuce_img, save=True)
        
        sandwich_tomato = Ingredient.objects.create(
            food_type=sandwich,
            name='Tomato',
            price=0.50,
            layer_order=6,
            is_default=False
        )
        stomato_img = self.download_image('https://images.unsplash.com/photo-1546094096-0df4bcaaa337?w=400&h=400&fit=crop', 'sandwich_tomato.jpg')
        if stomato_img:
            sandwich_tomato.image.save('sandwich_tomato.jpg', stomato_img, save=True)
        
        mayo = Ingredient.objects.create(
            food_type=sandwich,
            name='Mayonnaise',
            price=0.25,
            layer_order=7,
            is_default=False
        )
        mayo_img = self.download_image('https://images.unsplash.com/photo-1472476443507-c7a5948772fc?w=400&h=400&fit=crop', 'mayo.jpg')
        if mayo_img:
            mayo.image.save('mayo.jpg', mayo_img, save=True)
        
        mustard = Ingredient.objects.create(
            food_type=sandwich,
            name='Mustard',
            price=0.25,
            layer_order=8,
            is_default=False
        )
        mustard_img = self.download_image('https://images.unsplash.com/photo-1582169296194-e4d644c48063?w=400&h=400&fit=crop', 'mustard.jpg')
        if mustard_img:
            mustard.image.save('mustard.jpg', mustard_img, save=True)
        
        self.stdout.write(self.style.SUCCESS('Created Sandwich with ingredients'))
        
        # Create Dessert Category Items
        ice_cream = FoodType.objects.create(
            category=sweets,
            name='Ice Cream Sundae',
            base_price=3.99
        )
        ice_cream_img = self.download_image('https://images.unsplash.com/photo-1563805042-7684c019e1cb?w=400&h=400&fit=crop', 'ice_cream_sundae.jpg')
        if ice_cream_img:
            ice_cream.image.save('ice_cream_sundae.jpg', ice_cream_img, save=True)
        
        # Ice Cream Ingredients
        vanilla_ice_cream = Ingredient.objects.create(
            food_type=ice_cream,
            name='Vanilla Ice Cream',
            price=0.00,
            layer_order=1,
            is_default=True
        )
        vanilla_img = self.download_image('https://images.unsplash.com/photo-1497034825429-c343d7c6a68f?w=400&h=400&fit=crop', 'vanilla_ice_cream.jpg')
        if vanilla_img:
            vanilla_ice_cream.image.save('vanilla_ice_cream.jpg', vanilla_img, save=True)
        
        chocolate_sauce = Ingredient.objects.create(
            food_type=ice_cream,
            name='Chocolate Sauce',
            price=0.50,
            layer_order=2,
            is_default=False
        )
        choc_img = self.download_image('https://images.unsplash.com/photo-1511381939415-e44015466834?w=400&h=400&fit=crop', 'chocolate_sauce.jpg')
        if choc_img:
            chocolate_sauce.image.save('chocolate_sauce.jpg', choc_img, save=True)
        
        caramel_sauce = Ingredient.objects.create(
            food_type=ice_cream,
            name='Caramel Sauce',
            price=0.50,
            layer_order=3,
            is_default=False
        )
        caramel_img = self.download_image('https://bakerbynature.com/wp-content/uploads/2018/02/chocolatecaramelfudgesauce-1-of-1.jpg', 'caramel_sauce.jpg')
        if caramel_img:
            caramel_sauce.image.save('caramel_sauce.jpg', caramel_img, save=True)
        
        sprinkles = Ingredient.objects.create(
            food_type=ice_cream,
            name='Sprinkles',
            price=0.25,
            layer_order=4,
            is_default=False
        )
        sprinkles_img = self.download_image('https://images.unsplash.com/photo-1558961363-fa8fdf82db35?w=400&h=400&fit=crop', 'sprinkles.jpg')
        if sprinkles_img:
            sprinkles.image.save('sprinkles.jpg', sprinkles_img, save=True)
        
        whipped_cream = Ingredient.objects.create(
            food_type=ice_cream,
            name='Whipped Cream',
            price=0.50,
            layer_order=5,
            is_default=False
        )
        whipped_img = self.download_image('https://images.unsplash.com/photo-1571506165871-ee72a35bc9d4?w=400&h=400&fit=crop', 'whipped_cream.jpg')
        if whipped_img:
            whipped_cream.image.save('whipped_cream.jpg', whipped_img, save=True)
        
        cherry = Ingredient.objects.create(
            food_type=ice_cream,
            name='Cherry on Top',
            price=0.25,
            layer_order=6,
            is_default=False
        )
        cherry_img = self.download_image('https://images.unsplash.com/photo-1528821128474-27f963b062bf?w=400&h=400&fit=crop', 'cherry.jpg')
        if cherry_img:
            cherry.image.save('cherry.jpg', cherry_img, save=True)
        
        self.stdout.write(self.style.SUCCESS('Created Ice Cream Sundae with toppings'))
        
        self.stdout.write(self.style.SUCCESS('Database seeded successfully!'))
        self.stdout.write(self.style.WARNING('Note: Please add images manually to the media folder'))
