from django.http import HttpResponse


def index_api(request):
    return HttpResponse("Hello, this just test page.")