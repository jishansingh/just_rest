from rest_framework import serializers
from .models import NewUser
from .choices import CHOICE
from .lang import LANG
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=NewUser
        fields=('id','password','profession','language','pro',)