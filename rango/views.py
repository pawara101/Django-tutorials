from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

'''def index(request):
    return HttpResponse("<H1>Hello Pawara !!!!!</H1><H2>New App</H2>")'''

## To use template need to reconfigure index()
def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!

    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}

    #  Return a rendered response to send to the client.
    # 