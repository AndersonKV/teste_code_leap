import json

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

import requests
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

API_URL = 'https://dev.codeleap.co.uk/careers/'


@csrf_exempt
def create_post(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        title = request.POST.get('title')
        content = request.POST.get('content')

        data = {
            "username": username,
            "title": title,
            "content": content
        }

        response = requests.post("https://dev.codeleap.co.uk/careers/", json=data)

        return JsonResponse(response.json(), status=response.status_code)

    return render(request, 'criar_post.html')


def get_posts(request):
    if request.method == 'GET':
        response = requests.get(API_URL)
        return JsonResponse(response.json(), safe=False)


@csrf_exempt
def update_post(request, id):
    if request.method == 'PATCH':
        data = json.loads(request.body)
        response = requests.patch(f"{API_URL}{id}/", json=data)
        return JsonResponse(response.json(), status=response.status_code)


@csrf_exempt
def delete_post(request, id):
    if request.method == 'DELETE':
        response = requests.delete(f"{API_URL}{id}/")
        return JsonResponse({'mensagem': 'Post deletado com sucesso'}, status=response.status_code)
