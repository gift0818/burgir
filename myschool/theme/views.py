from django.shortcuts import render
def index(request):
    return render(request, 'base.html')

def mypage(request):
    return render(request, 'mypage.html')
