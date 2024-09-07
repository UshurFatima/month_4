from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models


# для полной информации
def post_detail_view(request, id):
    if request.method == "GET":
        post_id = get_object_or_404(models.Post, id=id)
        return render(
            request,
            template_name='post_detail.html',
            context={
                'post_id': post_id
            }
        )


# вывод неполной информации
def post_list_view(request):
    # два запроса: пост и гет; пост - приватные данные/когда пишем и
    # отправляем в бд, гет - выводим информацию
    if request.method == "GET":  # проверка на запрос
        # query запрос
        post_object = models.Post.objects.all()  # выводит все объекты из таблицы Пост
        return render(
            request,
            template_name='post_list.html',
            context={
                'post_object': post_object
            }
        )


def hello_view(request):
    return HttpResponse('hello world!!!')
