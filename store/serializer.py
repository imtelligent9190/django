from decimal import Decimal

from rest_framework import serializers

from store.models import Product, Collection, Review


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title', 'products_count']

    products_count = serializers.IntegerField(read_only=True)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'slug', 'inventory', 'unit_price', 'price_with_tax', 'collection']

    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')

    def calculate_tax(self, product):
        return round(product.unit_price * Decimal(1.1), 2)

class ReviewSerializer(serializers.ModelField):
    class Meta:
        model = Review
        fields = ['id','date','name','description','product']
    

    # def create(self, validated_data):
    #     product = Product(**validated_data)
    #     product.other=1
    #     product.save()
    #     return product

    # def update(self, instance, validated_data):
    #     instance.unit_price = validated_data.get('unit_price')
    #     instance.save()
    #     return instance

    # def validate(self, data):
    #     if data['password'] != data['confirm_password']:
    #         return serializers.ValidationError('Passwords do not match')
    #     return data

    # {
    #     "title": "a",
    #     "slug": "a",
    #     "inventory": 1,
    #     "unit_price": 1,
    #     "collection": 2
    # }
    #
    # {
    #     "title": "a",
    #     "unit_price": 1,
    #     "collection": 2
    # }
    #
    # {
    #     "title": "test"
    # }
