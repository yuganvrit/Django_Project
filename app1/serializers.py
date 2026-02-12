from rest_framework import serializers
from .models import Student,Book,Author,Course
from django.contrib.auth.models import User

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
        fields = ['name','age','email','grade','is_adult']







    # def to_internal_value(self, data):
    #     return data


    # def validate(self, attrs):
    #     age = attrs.get('age')
    #     if age > 5:
    #         raise serializers.ValidationError("Serailizer Age not must be greater than 5")
    #     return attrs
    

    # def update(self, instance, validated_data):
    #     return super().update(instance, validated_data)
    

    # def create(self, validated_data):
    #     return super().create(validated_data)
    

    # def to_representation(self, instance):
    #     #uppercase the name attribute of instance 
    #     # instance.name = instance.name.upper()
    #     # instance.adult = instance.is_adult
    #     # print(instance.adult)
    #     return super().to_representation(instance)




class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title','published_date']



class AuthorSerializer(serializers.ModelSerializer):
    books = BooksSerializer(many=True)
    class Meta:
        model = Author
        fields = ['name','birth_date','books']


    def validate(self, attrs):
        # #restrict the author older then 100 years 
        # birth_date = attrs.get('birth_date')
        # from datetime import date, timedelta
        # hundred_years_ago = date.today() - timedelta(days=365*100)

        # if birth_date  < hundred_years_ago:
        #     raise serializers.ValidationError("Author must be younger than 100 years old.")
        return super().validate(attrs)
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
    

    def create(self, validated_data):
        books = validated_data.pop('books')
        author = Author.objects.create(**validated_data)
        for book_data in books:
            Book.objects.create(author=author, **book_data)
        return author



class UserRegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username','email','password','confirm_password']


    def validate(self, attrs):
        password = attrs.get('password')
        confirm_password = attrs.get('confirm_password')
        if password != confirm_password:
            raise serializers.ValidationError("Password and confirm password does not match")
        return attrs
    

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        return super().create(validated_data)


    

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)


    class Meta():
        fields = ['username','password']





    


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course 
        fields = "__all__"