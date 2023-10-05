from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

items =[
    {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
    {"id": 2, "name": "Куртка кожаная","quantity":3},
    {"id": 5, "name": "Coca-cola1 литр","quantity":12},
    {"id": 7, "name": "Картофель фри","quantity":0},
    {"id": 8, "name": "Кепка","quantity":124}
]

def home(request):
    #text = """ <h1>" learn django"</h1>
     #     <strong>Автор</strong>: <i>Лебедкин А Д</i>
     #     """
    #return HttpResponse(text)
    context = {
        "name": "Петров Иван Николаевич",
        "email": "mymail@example.com"
    }
    
    return render(request, "index.html", context)


def about(request):
    textabout = """ <b>Имя: Андрей</b> <br>
                    <b>Отчество: Дмитриевич</b> <br>
                    <b>Фамилия: Лебедкин</b> <br>
                    <b>телефон:</b><br>
                    <b>e-mail: lebed202@mail.ru</b>  """
    return HttpResponse(textabout)

def get_item(request, id):   
    for item in items:
        if item['id'] == id:
            result = f"""
            <h2>Имя: {item["name"]} </h2>
            <p>Количество: {item["quantity"]}</p>
            <p><a href="/items">
        """
        return HttpResponse(result)
    return HttpResponseNotFound(f'Item with id={id} not found')




def items_list(request):
    result = "<h2>Список товаров</h2><ol>"
    for item in items:
        result += f"""<li><a href="/item/{item['id']}>"{item['name']}</a></li>"""
    result += '</ol>'
    return HttpResponse(result)




