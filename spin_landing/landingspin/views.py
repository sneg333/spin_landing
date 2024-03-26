from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Home, Onas, For, Five, SexBlock, Question, Category, Portfolio, Contact, Footer, Setting

# Страница дом
def home_page(request):
    home = Home.objects.all()
    onas = Onas.objects.all()
    fort = For.objects.all()
    five = Five.objects.all()
    sex = SexBlock.objects.all()
    question = Question.objects.all()

    categories = Category.objects.all()
    photos = Portfolio.objects.select_related('category')
    contact = Contact.objects.all()
    footer = Footer.objects.all()
    setting = Setting.objects.get(pk=1)

    context = {
        'home': home,
        'onas': onas,
        'fort': fort,
        'five': five,
        'sex': sex,
        'question': question,
        'categories': categories,
        'photos': photos,
        'contact': contact,
        'footer': footer,
        'setting': setting,

    }
    return render(request, 'page/home.html', context)

# Обработчик для несуществующих URL
def handler404(request, exception):
    return render(request, '404.html', {})