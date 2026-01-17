from django.http import HttpResponse

def my_blog(request):
    return HttpResponse("Blog home")
