from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from MainApp.models import Item

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
        
    try:
        item = Item.objects.get(id=item_id)        
    except Item.DoesNotExist:      
       return HttpResponseNotFound(f'Item with id={item_id} not found')
    else:
        context = {          
            "item": item
        }
        return render(request, "item-page.html", context)




    



def items_list(request):
    items = Item.objects.all()
    context = {
        "items": items
    }
    return render(request, "items-list.html", context)




