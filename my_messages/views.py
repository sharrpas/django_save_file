from http.client import HTTPResponse
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import MyMessages
from django.core import serializers
from pprint import pprint
import json

@csrf_exempt
def post_data(request):
    if request.method == 'POST':
        try:
            body_unicode = request.body.decode('utf-8')
            data = json.loads(body_unicode)
            newMessage = MyMessages.objects.create(**data)
            filterMessages = MyMessages.objects.filter(message = data["message"]).count()

            if filterMessages == 1:
                return JsonResponse ({'data': 'Your Message Saved'})
            
            return JsonResponse ({'This Message Count':filterMessages}, safe=False)
      
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON Data'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
   
    else:
        return JsonResponse({'error': 'Method Not Allowed'}, status=405)

