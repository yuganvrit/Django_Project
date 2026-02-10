from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import SimpleResponseSerializer
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from .serializers import StudentSerializer
from .random_class import Student
from .models import Student 
from .serializers import NewStudentSerializer,AuthorSerializer,UserRegisterSerializer,LoginSerializer
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework_simplejwt.tokens import RefreshToken
 
# class SimpleReponseView(APIView):
#     def get(self, request):
#         data = {
#             'message': 'hello word'
#             }
#         serializer = SimpleResponseSerializer(data=data)
#         serializer.is_valid(raise_exception=True)
#         print(type(serializer.data))
#         return Response(serializer.data)
    


# #function based view 

# # def hello_world(request):
# #     return HttpResponse('hello world')



# #function based view with multiple http methods 
# @api_view(['GET', 'POST','PATCH','PUT'])
# def hello_worlds(request):
#     if request.method == 'GET':
#         return Response({'name': 'Yugan','age':10})
#     elif request.method == 'POST':
#         print('hello world')
#         return HttpResponse('hello world from post')
    
#     elif request.method == 'PATCH':
#         return HttpResponse('hello world from patch')
    
#     return HttpResponse('hello world from other methods')


# @api_view(['GET'])
# def how_render_works_drf(request):
#     data = {"user": "admin", "action": "login", "timestamp": 2026}
#     json_data = JSONRenderer().render(data)
#     print(json_data)
#     print(type(json_data))
#     return HttpResponse(json_data, content_type='application/json')
#     # return Response(data)

        


# # from django.shortcuts import render
# # from django.shortcuts import render, redirect
# # from django.contrib.auth import login, authenticate, logout
# # from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# # from django.contrib import messages


# # def index(request):
# #     #we can pass dictionary as context to render
# #     context = {
# #         'name': 'Django',
# #         'version': '1.11'
# #     }
# #     return render(request, 'index.html', context)



# # def info(request):
# #     #we can pass dictionary as context to render
# #     context = {
# #         'name': 'Yugan',
# #         'age': '25'
# #     }
# #     return render(request, 'info.html', context)


# # # Signup View
# # def signup_view(request):
# #     if request.method == 'POST':
# #         print(request.POST)
# #         form = UserCreationForm(request.POST)
# #         if form.is_valid():
# #             user = form.save()
# #             login(request, user) # Log the user in after signup
# #             messages.success(request, "Registration successful.")
# #             return redirect('home') 
# #     else:
# #         form = UserCreationForm()
# #         context = {
# #             'form':form
# #         }
# #     return render(request, 'signup.html', context)

# # # Login View
# # def login_view(request):
# #     if request.method == 'POST':
# #         form = AuthenticationForm(request, data=request.POST)
# #         if form.is_valid():
# #             username = form.cleaned_data.get('username')
# #             password = form.cleaned_data.get('password')
# #             user = authenticate(username=username, password=password)
# #             if user is not None:
# #                 login(request, user)
# #                 return redirect('home')
# #         else:
# #             messages.error(request, "Invalid username or password.")
# #     else:
# #         form = AuthenticationForm()
# #     return render(request, 'login.html', {'form': form})




# # def home(request):
# #     return render(request, 'home.html')

# # # from django import forms
# # # from django.contrib.auth.forms import UserCreationForm
# # # from django.contrib.auth.models import User

# # # class ModernSignupForm(UserCreationForm):
# # #     def __init__(self, *args, **kwargs):
# # #         super().__init__(*args, **kwargs)
# # #         # Apply styling to every field in the form
# # #         for field_name, field in self.fields.items():
# # #             field.widget.attrs.update({
# # #                 'class': (
# # #                     'appearance-none block w-full px-10 py-3 border border-gray-300 '
# # #                     'rounded-lg placeholder-gray-400 focus:outline-none focus:ring-2 '
# # #                     'focus:ring-indigo-500 focus:border-transparent sm:text-sm transition-all'
# # #                 ),
# # #                 'placeholder': f'Enter your {field.label.lower()}'
# # #             })





# #post reqeust.data and send as response
# import json
# @api_view(['POST'])
# def echo_data(request):
#     #accept images from the request and send back as response
#     image = request.FILES.get('image')
#     print(type(image))
#     #image available attributes 
#     print(image.file)

#     print(image.name)
#     print(image.size)
#     print(image.content_type)

#     print(request.data)
#     return Response({
#         'image': image.name,
#         'image_size': image.size
#     })



# #show case example of request headers and params 

# @api_view(['GET'])
# def show_request_details(request):
#     headers = request.headers
#     category_value = request.query_params.get('category',None)
#     if category_value:
#         pass
#         #filter the dictionary 
    
#     return Response({
#         'headers': dict(headers),
        
#     })



# #classwork 

# #use params to filter a list of dictionary of items and return the filtered items as response

# #example list of items
# items = [
#     {'id': 1, 'name': 'item1', 'category': 'A'},
#     {'id': 2, 'name': 'item2', 'category': 'B'},
#     {'id': 3, 'name': 'item3', 'category': 'A'}
# ]

# #if params is passed as ?category=A then return only items with category A

# filtered_items = [
#     {'id': 1, 'name': 'item1', 'category': 'A'},
#     {'id': 3, 'name': 'item3', 'category': 'A'}
# ]

# @api_view(['GET'])
# def filter_items(request):
#     items = [
#     {'id': 1, 'name': 'item1', 'category': 'A'},
#     {'id': 2, 'name': 'item2', 'category': 'B'},
#     {'id': 3, 'name': 'item3', 'category': 'A'}]
#     category_value = request.query_params.get('category', None)
#     if category_value:
#         filtered_items = [item for item in items if category_value == item['category']]

#     else:
#         filtered_items = items

#     return Response({
#         'items': filtered_items
#     })



# # create a class name with student

# @api_view(['GET'])
# def display_student_data(request):
#     first_student = Student('Ram',10,5)
#     serializer = StudentSerializer(first_student)
#     return Response(serializer.data)


# #classwork
# #create a function based view 
# #that serailizer instance of pizza class 
# #also create a serializer for pizza class
# #and return the serialized data as response


# @api_view(['POST'])
# def create_student_data(request):
#     print(type(request))
#     print(request.data)
#     serializer = StudentSerializer(data=request.data,many=True)
#     if serializer.is_valid():
#         print(serializer.validated_data)
#         container_to_store_students_data = []
#         for data in serializer.validated_data:
#             instance = Student(data['name'],data['grade'],data['gpa'])
#             container_to_store_students_data.append(instance)
#         return Response({'message':'Student data created successfully'})
#     else:
#         return Response(serializer.errors, status=400)
            

        
    

@api_view(['GET','POST'])
def get_or_create_student(request):
    print(request.method)
    if request.method == 'GET':
        all_students = Student.objects.all()
        serializer = NewStudentSerializer(all_students,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
        
    else:
        serializer = NewStudentSerializer(data=request.data,many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    



@api_view(['POST'])
def create_books_with_author (request):
    serializer = AuthorSerializer(data=request.data)
    serializer.is_valid(raise_exception=True) #validate method will be called 
    serializer.save()  #serializer create method will be called
    return Response('books and author has been created', status=status.HTTP_201_CREATED)
    




from django.contrib.auth.models import User



@api_view(['POST','GET'])
def register_user(request):
    if request.method == 'POST':
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)

    else:
        users = User.objects.all()
        serializer = UserRegisterSerializer(users,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    


@api_view(['POST'])
def login_user(request):
    serializer = LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    print(serializer.validated_data)
    print(type(serializer.validated_data))

    #get the username and password
    username = serializer.validated_data.get('username')
    password = serializer.validated_data.get('password')

    #authentication
    user = authenticate(request,username=username,password=password)
    print(user)

    #if user is not found 
    if not user:
        return Response({'error':'Invalid credentials'},status=status.HTTP_401_UNAUTHORIZED)

    # #if user is found 
    # #return auth token 
    # token,created = Token.objects.get_or_create(user=user)
    # print(token)
    token = RefreshToken.for_user(user)
    access_token = token.access_token
    refresh_token = token
    return Response({
        'access_token':str(access_token),
        'refresh_token':str(refresh_token)
    },
    status=status.HTTP_200_OK
    )



#protected endpoint

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def simple_hello_world(request):
    return Response({'msg':'hello world'},status=status.HTTP_200_OK)





    


