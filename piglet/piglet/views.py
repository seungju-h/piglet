from django.shortcuts import render

def main(request):
    return render(request, "main.html")

def login(request):
    return render(request, "login.html")

def missinglist(request):
    return render(request, "missinglist.html")

def missinglistdetail(request):
    return render(request, "missinglistdetail.html")

def reportmissing(request):
    return render(request, "reportmissing.html")

def eventpage1(request):
    return render(request, "eventpage1.html")
def eventpage2(request):
    return render(request, "eventpage2.html")
def eventpage3(request):
    return render(request, "eventpage3.html")