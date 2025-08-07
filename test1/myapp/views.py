from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
   
    q=request.GET['answer']
    return render(request,'index.html', {'anser':q})
    
# def count(request):
#     word=request.GET['answer']
     
#     return render(request,'cnt.html',{'answer':word})