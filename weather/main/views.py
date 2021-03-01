from django.shortcuts import render


def index(request):
    """Контроллер главной страницы"""
    data = {
        'title': 'Главная страница',
        'values': ['Some', 'Hello', '123'],
        'obj': {
            'car': 'BMW',
            'age': 18,
            'hobby': 'football'
        }
    }
    return render(request, 'main/index.html', data)


def about(request):
    """Контроллер страницы main/about.html"""
    return render(request, 'main/about.html')
