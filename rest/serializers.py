from rest_framework import serializers
from .models import NewUser
from .choices import CHOICE
from .lang import LANG
class UserSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField(max_length=20)
    password=serializers.CharField(max_length=20)
    profession=serializers.ChoiceField(choices=CHOICE,required=True)
    language=serializers.ChoiceField(choices=LANG,required=False)
    pro=serializers.BooleanField(required=False)
    
    def create(self,postdata):
        user=NewUser.objects.create(**postdata)
        return user
    def update(self,instance,postdata):
        name=postdata.get('name',instance.name)
        password=postdata.get('password',instance.password)
        profession=postdata.get('profession',instance.profession)
        language=postdata.get('language',instance.language)
        pro=postdata.get('pro',instance.pro)
        instance.save()
        return instance