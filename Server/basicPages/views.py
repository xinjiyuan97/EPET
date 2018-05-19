from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def pageNotFound(request):
    return render(request, 'errorPage.html', {'errorCode': 404})

def permissionDenied(request):
    return render(request, 'errorPage.html', {'errorCode': 403})

def pageError(request):
    return render(request, 'errorPage.html', {'errorCode': 500})
