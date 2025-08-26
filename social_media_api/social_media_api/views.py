from django.http import JsonResponse
from django.http import HttpResponse

def home(request):
    return JsonResponse({"message": "Welcome to the Social Media API"})
    return HttpResponse("Welcome to the Social Media API! Visit /api/accounts/ for accounts endpoints.")
