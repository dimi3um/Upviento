from django.shortcuts import render


# Create your views here.
def index(request):
    ctx = {'message': "Under construction"}
    return render(request, 'signup/index.html', context=ctx)
