# Generated by Django 3.2.12 on 2024-03-04 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingspin', '0013_question_home'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='вопрос')),
                ('portfolio_image', models.ImageField(blank=True, upload_to='image_portfolio', verbose_name='портфолио')),
                ('category', models.ManyToManyField(blank=True, to='landingspin.Category', verbose_name='категории')),
            ],
            options={
                'verbose_name': 'Портфолио',
                'verbose_name_plural': 'Портфолио',
            },
        ),
    ]
