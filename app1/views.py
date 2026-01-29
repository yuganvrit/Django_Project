from rest_framework.views import APIView
from rest_framework.response import Response
from.serilizer import SimpleResponseSerializer
from rest_framework.decorators import api_view
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from .random_class import Pizza
from .serializers import PizzaSerializer
#model serializer
from .models import Teacher
from .serializers import NewTeacherSerializer
from rest_framework import status



class SimpleResposeView(APIView):

    def get(self,request):
        data={
            'message':'hello world'
        }
        serializer=SimpleResponseSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)
    
def hello_world(request):
    return HttpResponse("Hello bro")

@api_view(['GET'])
def how_render_works_drf(request):
    data={"user":"admin","action":"login","timestamp":2026}
    json_data=JSONRenderer().render(data)
    print(json_data)
    print(type(json_data))

    return HttpResponse(json_data,content_type='application/json')


# from django.shortcuts import render

# # Create your views here. 
# def index(request):
#     context={
#         'name':'Django',
#         'version':'1.11'#yo garnuko matalab index.html bhitra pass garna sakxau
#     }
#     return render(request,'index.html',context)

# def new(request):
#     context1={
#         'name':'Django',
#         'version':'1.11'#yo garnuko matalab index.html bhitra pass garna sakxau
#     }
#     return render(request,'new.html',context1)



@api_view(['GET','POST','DELETE','PUT'])
def dict_operation(request):
    data = {
        'name':'suman',
        'age':22,
        'address':'pimbal'
    }

    if request.method == 'POST':
        data['hometown'] = 'kalikot' 
    
    elif request.method == 'GET':
        pass
    
    elif request.method == 'DELETE':
        data.pop('address')
    
    else:
        data['name'] = 'suman'

    return Response(data)
#use params(GET ma paraya jasto) to ,filter a list of dictonary  of items and retiurn the filtered item as responseite,
@api_view(['GET'])
def Params(request):#This decorator only work using get
    items=[
        {'id':1,'name':'item1','category':'A'},
        {'id':2,'name':'item2','category':'B'},
        {'id':3,'name':'item2','category':'A'}
          
    ]
    headers=request.headers#category xa bhane line nattra naline
    category_value=request.query_params.get('category',None)#Query_params build in ani kun kun search garne tini harulai lageko xa
    if category_value:
        filter_items=[#hold in ..iteration ani condition....
            item for item in items
            if item['category']==category_value

        ]
    else:
        filter_items=items #filter nagarepaxi sabai dekhayo

    return Response(filter_items)


#create a function based view
#that serializer instance of pizza class
#also create a serializer for pizza class
#return the serializer data as response
# 🔑 MAIN CONCEPT

# Django REST Framework uses serializers to convert Python class objects into JSON so they can be sent as API responses.
# That’s it. That’s the core idea.
# 🧠 Slightly expanded (still simple)
# A normal Python class (Pizza) holds data
# A serializer knows how to read that object
# The view connects everything
# DRF returns JSON, not Python objects

# @api_view(['GET'])
# def display_pizza_data(request):
#     pizza = Pizza("American", 275, 4.5)   # Pizza class instance
#     serializer = PizzaSerializer(pizza)  # serialize instance #dic maa lageko xa
#     return Response(serializer.data)

# for modelserializer..fro create POST status
@api_view(['GET','POST'])#aru call garda 405 method is not allowed
def get_or_create_teacher(request):
    print(request.method)
    if request.method=='GET':
        all_Teacher=Teacher.objects.all()#select * from public stdent...scl maa sikeko..Student is model
        print(all_Teacher)#queryset ..list nai ho
        serializer=NewTeacherSerializer(all_Teacher,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        serializer=NewTeacherSerializer(data=request.data,many=True)
        serializer.is_valid(raise_exception=True)#jahile is_valid check garnu parne hunxa
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)





