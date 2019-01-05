from rest_framework import serializers
from wishes.models import Wish

class WishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wish
        fields = ('id','title','wishtext')

