from rest_framework import serializers
from product.models import Product
from product.constants import SIZE_TYPE

class ProductSerializer(serializers.ModelSerializer):
    size = serializers.MultipleChoiceField(choices=SIZE_TYPE)

    class Meta:
        model = Product
        fields = "__all__"

    def to_representation(self, instance):
        represent = super().to_representation(instance)
        represent["size"] = instance.size.split(",")
        return represent
    
    def validate_size(self, value):
        return ",".join(value)