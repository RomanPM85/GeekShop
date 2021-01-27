from django.shortcuts import render

# Create your views here.

def index(request):
    content = {
        'title': 'geekShop',
    }
    return render(request, 'mainapp/index.html', content)

def products(request):
    content = {
        'title': 'geekShop - catalog',
        'products': [
            {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': '6 090,00 руб.',
             'cardtext': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.'},
            {'name': 'Синяя куртка The North Face', 'price': '23 725,00 руб.',
             'cardtext': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.'},
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': '3 390,00 руб.',
             'cardtext': 'Материал с плюшевой текстурой. Удобный и мягкий.'},
            {'name': 'Черный рюкзак Nike Heritage', 'price': '2 340,00 руб.',
             'cardtext': 'Плотная ткань. Легкий материал.'},
            {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex',
             'price': '13 590,00 руб.', 'cardtext': 'Гладкий кожаный верх. Натуральный материал.'},
            {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN<',
             'price': '2 890,00 руб.', 'cardtext': 'Легкая эластичная ткань сирсакер Фактурная ткань.'},
        ],

    }
    return render(request, 'mainapp/products.html', content)