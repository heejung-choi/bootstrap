# django import style guide
# 1. standard library
# 2. 3rd party library
# 3. django
# 4. local django
 
import random
from datetime import datetime
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')


def dinner(request):
    foods = ['족발', '햄버거', '치킨', '초밥']
    pick = random.choice(foods)
    context = {
        'pick': pick,
    }
    return render(request, 'dinner.html', context)


def image(request):
    image_url = 'https://picsum.photos/200/300.jpg'
    context = {
        'image_url': image_url,
    }
    return render(request, 'image.html', context)


def hello(request, name):
    context = {
        'name': name,
    }
    return render(request, 'hello.html', context)


def introduce(request, name, age):
    context = {
        'name': name,
        'age': age,
    }
    return render(request, 'introduce.html', context)


def times(request, num1, num2):
    result = num1 * num2
    context = {
        'num1': num1,
        'num2': num2,
        'result': result,
    }
    return render(request, 'times.html', context)


def dtl_practice(request):
    foods = ['짜장면', '초밥', '차돌짬뽕', '콩국수']
    empty_list = []
    messages = 'Life is short, You need Python'
    datetime_now = datetime.now()
    context = {
        'foods': foods,
        'empty_list': empty_list,
        'messages': messages,
        'datetime_now': datetime_now,
    }
    return render(request, 'dtl_practice.html', context)


def ispal(request, word):
    if word == word[::-1]:
        result = True
    else:
        result = False
    context = {
        'result': result,
    }
    return render(request, 'ispal.html', context)