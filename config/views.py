from django.http.response import HttpResponse, JsonResponse

# function-base view
def hello_world(request):
    return HttpResponse("Hello, World!")

def hello_world_json(request):
    return JsonResponse({"message":"Hello, World!"})
