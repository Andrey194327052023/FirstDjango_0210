from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    text = """ <h1>" learn django"</h1>
          <strong>Автор</strong>: <i>Лебедкин А Д</i>
          """
    return HttpResponse(text)


def about(request):
    textabout = """ <b>Имя: Андрей</b> <br>
                    <b>Отчество: Дмитриевич</b> <br>
                    <b>Фамилия: Лебедкин</b> <br>
                    <b>телефон:</b><br>
                    <b>e-mail: lebed202@mail.ru</b>  """
    return HttpResponse(textabout)
