from rest_framework import serializers
from .models import Student,Book,Author

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




    


