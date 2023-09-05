from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
import json
import os
from .models import Dish,Order
from decimal import Decimal

# Create your views here.
def menushow(request):
    all_dishes = Dish.objects.all()
    return render(request,'index.html',{'dishes':all_dishes})

def addDish(request):
    if request.method=='POST':
        # dish_id=request.POST["id"]
        name=request.POST['name']
        price=request.POST['price']
        availability=request.POST['availability']

        dish1 = Dish(name=name, price=price, availability=availability)
        dish1.save()
        return redirect('menu')
    return render(request, 'add.html')


def DeleteDish(request,id):
    if request.method=='POST':
        document = Dish.objects.get(id=id)
        document.delete()
        return redirect('menu')
        
def UpdateDish(request,id):
    order_instance = Dish.objects.get(id=id)
    if request.method=='POST':
         name=request.POST['name']
         price=request.POST['price']
         availability=request.POST['availability']
         order_instance.name=name
         order_instance.price=price
         order_instance.availability=availability
         order_instance.save()
         return redirect('menu')
    else:
        document = Dish.objects.get(id=id)
        return render(request, 'update.html',{'dish':document})
    
def TakeOrder(request):
    if request.method=='POST':
        name=request.POST['customer_name']
        selected_dishes = request.POST.getlist('selected_dishes')
        selected_dish_objects=Dish.objects.filter(id__in=selected_dishes)
        selected_dishes_list = [{'name': dish.name, 'price':str(dish.price)} for dish in selected_dish_objects]
        #selected_dishes_json = json.dumps(selected_dishes_list, default=str)
        order1=Order(customer_name=name,dishes=selected_dishes_list,status="received")
        order1.save()
        return redirect('menu')

    else:
        Available_items = Dish.objects.filter(availability="yes")
        return render(request,'placeorder.html',{'dishes':Available_items})


def reviewOrder(request):
    data=Order.objects.all()
    return render(request,'order.html',{'orders':data})
    
def UpdateStatus(request,orderID):
    order_instance = Order.objects.get(id=orderID)
    if request.method=='POST':
        stat=request.POST["status"]
        
        order_instance.status = stat
        order_instance.save()
        return redirect('order')       
    return render(request,'updateorder.html',{'order':order_instance})
    
    
               

           



    
         
    





        