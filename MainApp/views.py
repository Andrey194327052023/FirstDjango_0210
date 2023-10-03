from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    text = """ <h1>" learn django"</h1>
          <strong>Автор</strong>: <i>Лебедкин А Д</i>
          """
    return HttpResponse(text)