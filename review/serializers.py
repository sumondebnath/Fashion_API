from rest_framework import serializers
from review.models import Review

class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"