from django.shortcuts import render
from django.http import HttpResponse
import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect

# Create your views here.
data=None
def iot(request):

    return render(request,'index4.html')

@csrf_exempt
def receive_json_data(request):
    global data
    if request.method == 'POST':
        try:
            json_data = json.loads(request.body)
            data=json_data
        except json.decoder.JSONDecodeError:
            return JsonResponse({'message': 'Invalid JSON data'}, status=400)
    else:
        return JsonResponse({'message': 'Method not allowed'}, status=405)

def send_json_data(request):
    global data
    return JsonResponse(data)
