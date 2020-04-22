from django.http import HttpResponse

def test(request):
    return HttpResponse('<strong>Static test</strong>')

def test_param(request, param):
    return HttpResponse(f'<strong>{param}</strong>')