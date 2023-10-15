from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from MainApp.models import Item

# Create your views here.



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
    author = {
    "Имя": "Иван",
    "Отчество": "Петрович",
    "Фамилия": "Иванов",
    "телефон": "8-923-600-01-02",
    "email": "vasya@mail.ru"

    }
    result = f""" 
    <header>
        /<a href="/">Home</a> / <a href="/items">Items</a> / <a href="/about">About</a>
    </header>
    Имя: <b> {author['Имя']}</b> <br>
    Отчество: <b>{author['Отчество']}</b> <br>
    Фамилия: <b>{author['Фамилия']}</b> <br>
    Телефон:<b>{author['Телефон']}</b><br>
    email: <b>{author['email']}</b>  
    """
    return HttpResponse(result)

def get_item(request, item_id):
        
    try:
        item = Item.objects.get(id=item_id)
        colors = []
        # Проверяем, есть ли хоть один цвет у товара
        if item.colors.exists():
            colors = item.colors.all()
     
    except Item.DoesNotExist:      
       return HttpResponseNotFound(f'Item with id={item_id} not found')
    else:
        context = {          
            "item": item,
            "colors": colors
        }
        return render(request, "item-page.html", context)




    



def items_list(request):
    items = Item.objects.all()
    context = {
        "items": items
    }
    return render(request, "items-list.html", context)




