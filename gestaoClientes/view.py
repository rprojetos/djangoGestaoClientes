from django.http import HttpResponse
def hello(request):
    return HttpResponse("<h1>Hello Word!</h1>")

def getnum(request, num):
    return HttpResponse(f"<h2>O número passado via get foi {num}</h2>")

    