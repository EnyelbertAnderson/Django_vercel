from django.http import HttpResponse

def hola_mundo(request):
    return HttpResponse("Hola mundo, mi nombre es Enyelbert")
