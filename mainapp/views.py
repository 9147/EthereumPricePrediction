from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .prediction import predict_price_for_future_random_forest

def home(request):
    return render(request,'home.html')

def predict(request):
    if request.method == 'POST':
        print(request.POST)
        date = request.POST['date']
        print(date)
        predicted_price = predict_price_for_future_random_forest(date)
        predicted_price = round(predicted_price, 2)
        return JsonResponse({'predicted_price': predicted_price})
    else:
        return HttpResponse(status=405)
