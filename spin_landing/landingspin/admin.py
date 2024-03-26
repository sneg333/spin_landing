from django.contrib import admin
from .models import Home, Onas, For, Five, SexBlock, Question, Category, Portfolio, Contact, Footer, Setting

'''Домашняя'''
admin.site.register(Home)

'''блок о нас'''
admin.site.register(Onas)

'''производители'''
admin.site.register(For)

'''ассортимент'''
admin.site.register(Five)

'''Наша продукция'''
admin.site.register(SexBlock)

'''вопросы'''
admin.site.register(Question)

'''категории для портфолио'''
admin.site.register(Category)

'''портфолио'''
admin.site.register(Portfolio)

'''контакты'''
admin.site.register(Contact)

'''футтер'''
admin.site.register(Footer)

'''Модель Title'''
admin.site.register(Setting)





