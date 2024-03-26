from django.db import models

# модель карусели на главной странице

'''домашняя страница'''
class Home(models.Model):
    title = models.CharField(max_length=255, verbose_name='заголовок')
    title2 = models.CharField(max_length=500, verbose_name='второе слово заголовка')
    pod_title2 = models.CharField(max_length=255, verbose_name='текст под заголовком')

    class Meta:
        verbose_name = 'домашняя'
        verbose_name_plural = 'домашняя'

    def __str__(self):
        return self.title

'''о нас'''
class Onas(models.Model):
    title = models.CharField(max_length=255, verbose_name='титл о нас')
    title2 = models.CharField(max_length=255, verbose_name='текст под титл')
    onasimage = models.ImageField(upload_to='image_onas', blank=True, verbose_name='картинка онас')
    title3 = models.CharField(max_length=255, verbose_name='титл три')
    title4 = models.CharField(max_length=255, verbose_name='титл четыре')
    title5 = models.TextField(blank=True, verbose_name='текст')
    home = models.ForeignKey(Home, on_delete=models.CASCADE, related_name='onas')
    title6 = models.TextField(blank=True, verbose_name='текст описание')

    class Meta:
        verbose_name = 'о нас'
        verbose_name_plural = 'о нас'

    def __str__(self):
        return self.title
    
'''производители'''    
class For(models.Model):
    title = models.CharField(max_length=255, verbose_name='заголовок')
    title2 = models.CharField(max_length=255, verbose_name='текст под титл1')
    title3 = models.CharField(max_length=255, verbose_name='текст под титл2')
    title4 = models.CharField(max_length=255, verbose_name='текст под титл3')
    image = models.ImageField(upload_to='for', verbose_name='фото for', blank=True)
    home = models.ForeignKey(Home, on_delete=models.CASCADE, related_name='fort')

    class Meta:
        verbose_name = 'производители'
        verbose_name_plural = 'производители'

    def __str__(self):
        return self.title

'''блок ассортимент'''    
class Five(models.Model):
    title = models.CharField(max_length=255, verbose_name='5 заголовок')
    title2 = models.CharField(max_length=500, verbose_name='5 текст под титл')
    image = models.ImageField(upload_to='5class', verbose_name='фото 5 блока', blank=True)
    text5 = models.TextField(blank=True, verbose_name='5 блок текст описание')
    home = models.ForeignKey(Home, on_delete=models.CASCADE, related_name='five')

    class Meta:
        verbose_name = 'ассортимент'
        verbose_name_plural = 'ассортимент'

    def __str__(self):
        return self.title
    
'''Наша продукция'''
class SexBlock(models.Model):
    title = models.CharField(max_length=255, verbose_name='6 блок', blank=True)
    network_image = models.ImageField(upload_to='image_6_block', blank=True, verbose_name='картинка 6 блока')
    title1 = models.CharField(max_length=500, verbose_name='6 блокпод фото', blank=True)
    title2 = models.CharField(max_length=500, verbose_name='6 блок текст', blank=True)
    home = models.ForeignKey(Home, on_delete=models.CASCADE, related_name='sexblock')

    class Meta:
        verbose_name = 'Наша продукция'
        verbose_name_plural = 'Наша продукция'

    def __str__(self):
        return self.title
    
'''Вопрос ответ'''
class Question(models.Model):
    title_question = models.CharField(max_length=500, verbose_name='вопрос')
    body_question = models.TextField(blank=True, default='', verbose_name='ответ')
    home = models.ForeignKey(Home, on_delete=models.CASCADE, related_name='question')

    class Meta:
        verbose_name = 'вопросы'
        verbose_name_plural = 'вопросы'

    def __str__(self):
        return self.title_question

'''Категории для портфолио'''
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
    
'''Портфолио'''
class Portfolio(models.Model):
    title = models.CharField(max_length=500, verbose_name='title')
    portfolio_image = models.ImageField(upload_to='image_portfolio', blank=True, verbose_name='портфолио')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'Портфолио'
        verbose_name_plural = 'Портфолио'

    def __str__(self):
        return self.title

'''Контакты'''
class Contact(models.Model):
    title1 = models.CharField(max_length=500, verbose_name='title1')
    title2 = models.CharField(max_length=500, verbose_name='title2')
    title3 = models.CharField(max_length=500, verbose_name='title3')
    location = models.CharField(max_length=500, verbose_name='адрес')
    email = models.CharField(max_length=500, verbose_name='email')
    tel = models.CharField(max_length=500, verbose_name='tel')
    
    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return self.title1
    
'''футтер'''
class Footer(models.Model):
    title = models.CharField(max_length=500, verbose_name='title')
    title1 = models.CharField(max_length=500, verbose_name='title1')
    title2 = models.CharField(max_length=500, verbose_name='title2')
    title3 = models.CharField(max_length=500, verbose_name='title3')
    title4 = models.CharField(max_length=500, verbose_name='title4')
    title5 = models.CharField(max_length=500, verbose_name='title5')

    class Meta:
        verbose_name = 'Футер'
        verbose_name_plural = 'Футер'

    def __str__(self):
        return self.title

'''Модель title'''
class Setting(models.Model):
    objects = None
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayir')
    )
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='media/', blank=True)

    def __str__(self):
        return self.title



