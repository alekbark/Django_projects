import requests
from django.shortcuts import render

def items_list(request):
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    items = response.json()[:10]

    return render(request, 'main/list.html', {'items': items})

def items_detail(request, id):
    response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{id}')
    item = response.json()

    return render(request, 'main/card.html', {'item': item})
