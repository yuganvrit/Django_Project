from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
    grade = serializers.IntegerField()
    name = serializers.CharField()
    gpa = serializers.IntegerField()
    

    class Meta():
        fields = ['name','grade','gpa']


    def validate(self, attrs):
        #validate gpa 
        gpa = attrs.get('gpa')
        if gpa <= 0 or gpa >= 4:
            raise serializers.ValidationError('GPA must be between 0 and 4')
        return attrs
    



class NewStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"



    


