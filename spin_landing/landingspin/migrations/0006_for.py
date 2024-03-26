# Generated by Django 3.2.12 on 2024-03-03 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingspin', '0005_onas_title6'),
    ]

    operations = [
        migrations.CreateModel(
            name='For',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='заголовок')),
                ('title2', models.CharField(max_length=255, verbose_name='текст под титл1')),
                ('title3', models.CharField(max_length=255, verbose_name='текст под титл2')),
                ('title4', models.CharField(max_length=255, verbose_name='текст под титл3')),
            ],
            options={
                'verbose_name': 'четвёртый блок',
                'verbose_name_plural': 'четвёртый блок',
            },
        ),
    ]
