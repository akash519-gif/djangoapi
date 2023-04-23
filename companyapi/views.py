from django.http import JsonResponse


def home_page(request):
    print("home page requested")
    friends=[
        'ankit',
        'ravi',
        'uttam'
    ]
    return JsonResponse(friends,safe=False)