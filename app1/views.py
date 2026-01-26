from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import SimpleResponseSerializer
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer

class SimpleReponseView(APIView):
    def get(self, request):
        data = {
            'message': 'hello word'
            }
        serializer = SimpleResponseSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        print(type(serializer.data))
        return Response(serializer.data)
    


#function based view 

# def hello_world(request):
#     return HttpResponse('hello world')



#function based view with multiple http methods 
@api_view(['GET', 'POST','PATCH','PUT'])
def hello_worlds(request):
    if request.method == 'GET':
        return Response({'name': 'Yugan','age':10})
    elif request.method == 'POST':
        print('hello world')
        return HttpResponse('hello world from post')
    
    elif request.method == 'PATCH':
        return HttpResponse('hello world from patch')
    
    return HttpResponse('hello world from other methods')


@api_view(['GET'])
def how_render_works_drf(request):
    data = {"user": "admin", "action": "login", "timestamp": 2026}
    json_data = JSONRenderer().render(data)
    print(json_data)
    print(type(json_data))
    return HttpResponse(json_data, content_type='application/json')
    # return Response(data)

        


# from django.shortcuts import render
# from django.shortcuts import render, redirect
# from django.contrib.auth import login, authenticate, logout
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib import messages


# def index(request):
#     #we can pass dictionary as context to render
#     context = {
#         'name': 'Django',
#         'version': '1.11'
#     }
#     return render(request, 'index.html', context)



# def info(request):
#     #we can pass dictionary as context to render
#     context = {
#         'name': 'Yugan',
#         'age': '25'
#     }
#     return render(request, 'info.html', context)


# # Signup View
# def signup_view(request):
#     if request.method == 'POST':
#         print(request.POST)
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user) # Log the user in after signup
#             messages.success(request, "Registration successful.")
#             return redirect('home') 
#     else:
#         form = UserCreationForm()
#         context = {
#             'form':form
#         }
#     return render(request, 'signup.html', context)

# # Login View
# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')
#         else:
#             messages.error(request, "Invalid username or password.")
#     else:
#         form = AuthenticationForm()
#     return render(request, 'login.html', {'form': form})




# def home(request):
#     return render(request, 'home.html')

# # from django import forms
# # from django.contrib.auth.forms import UserCreationForm
# # from django.contrib.auth.models import User

# # class ModernSignupForm(UserCreationForm):
# #     def __init__(self, *args, **kwargs):
# #         super().__init__(*args, **kwargs)
# #         # Apply styling to every field in the form
# #         for field_name, field in self.fields.items():
# #             field.widget.attrs.update({
# #                 'class': (
# #                     'appearance-none block w-full px-10 py-3 border border-gray-300 '
# #                     'rounded-lg placeholder-gray-400 focus:outline-none focus:ring-2 '
# #                     'focus:ring-indigo-500 focus:border-transparent sm:text-sm transition-all'
# #                 ),
# #                 'placeholder': f'Enter your {field.label.lower()}'
# #             })