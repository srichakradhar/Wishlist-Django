from rest_framework import serializers
from wishes.models import Wish
from django.contrib.auth.models import User

class WishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wish
        fields = ('id','title','wishtext')

class UserSerializer(serializers.Serializer):
    wishes = serializers.PrimaryKeyRelatedField(many=True, queryset=Wish.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'wishes')
