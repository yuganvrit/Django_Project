from rest_framework import serializers
from .models import Teacher

class NewTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model=Teacher
        fields="__all__"



class PizzaSerializer(serializers.Serializer):
    name=serializers.CharField()
    price=serializers.IntegerField()
    size=serializers.IntegerField()
    #mathi ko satta ma sidai modelserializer use garne


#FOr models serializer of student mathi ko bhanda kam ...auto deffines

