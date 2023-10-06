from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

autor = {
    "Имя": "Иван",
    "Отчество": "Петрович",
    "Фамилия": "Иванов",
    "Телефон": "89236000102",
    "email": "vasya@mail.ru"
}

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
    result = f""" 
    <header>
        /<a href="/">Home</a> / <a href="/items">Items</a> / <a href="/about">About</a>
    </header>
    Имя: <b> {autor['Имя']}</b> <br>
    Отчество: <b>{autor['Отчество']}</b> <br>
    Фамилия: <b>{autor['Фамилия']}</b> <br>
    Телефон:<b>{autor['Телефон']}</b><br>
    email: <b>{autor['email']}</b>  
    """
    return HttpResponse(result)

def get_item(request, item_id):
     
    #for item in items:
    #    if item['id'] == id:
    #        result = f"""
    #        <h2>Имя: {item["name"]} </h2>
    #        <p>Количество: {item["quantity"]}</p>
    #        <p><a href="/items">Назад к списку товаров</a></p>
    #    """
    #    return HttpResponse(result)
    item = next((item for item in items if item["id"] == item_id), None)
    if item:
        context = {
            "item": item
        }
        return render(request, "item-page.html", context)
    return HttpResponseNotFound(f'Item with id={id} not found')




def items_list(request):
    #result = "<h2>Список товаров</h2><ol>"
    #for item in items:
    #    result += f"""<li><a href="/item/{item['id']}>"{item['name']}</a></li>"""
    #result += '</ol>'
    #return HttpResponse(result)
    context = {
        "items": items
    }
    return render(request, "items-list.html", context)




