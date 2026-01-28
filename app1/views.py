from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET','POST','PUT','DELETE'])
def home(request):
    my_dictionary = {'a':"apple",'b':"banana",'c':"cat"}
    if request.method == "GET":
        return Response(my_dictionary)
    
    if request.method == "POST":
        my_dictionary.update({'d':"dog"})
        return Response(my_dictionary)
    
    if request.method == "PUT":
        my_dictionary.update({'a':"aeroplane"})
        return Response(my_dictionary)
    
    if request.method == "DELETE":
        my_dictionary.pop('a')
        return Response(my_dictionary)

# Create your views here.
@api_view(['GET'])
def filter(request):
    items = [
        {'id':1, 'name':'item1', 'category':'A'},
        {'id':2, 'name':'item2', 'category':'B'},
        {'id':3, 'name':'item3', 'category':'A'},
        {'id':4, 'name':'item4', 'category':'B'},
    ]

    category_value = request.query_params.get('category', None)

    filtered_item = []
    for item in items:
        if item['category'] == category_value:
            filtered_item.append(item)


    print(filtered_item)
    
    return Response(filtered_item)
