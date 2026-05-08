from django.http import JsonResponse

def api(request):
    data = [i for i in range(10)]
    return JsonResponse(data, safe=False)