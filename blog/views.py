from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models, forms


def post_list_edit_view(request):
    if request.method == "GET":  # проверка на запрос
        # query запрос
        post_object = models.Post.objects.all()  # выводит все объекты из таблицы Пост
        return render(
            request,
            template_name='crud/post_list_edit.html',
            context={
                'post_object': post_object
            }
        )


def update_post_view(request, id):
    post_id = get_object_or_404(models.Post, id=id)
    if request.method == 'POST':
        form = forms.PostForm(request.POST, instance=post_id)
        if form.is_valid():
            form.save()
            return HttpResponse('Новость отредактирована!!! <a href = "/post_list/">На список новостей</a>')
    else:
        form = forms.PostForm(instance=post_id)

    return render(
        request,
        template_name='crud/update_post.html',
        context={
            'form': form,
            'post_id': post_id
        }
    )


def post_list_delete_view(request):
    if request.method == "GET":  # проверка на запрос
        # query запрос
        post_object = models.Post.objects.all()  # выводит все объекты из таблицы Пост
        return render(
            request,
            template_name='crud/post_list_delete.html',
            context={
                'post_object': post_object
            }
        )


def post_drop_view(request, id):
    post_id = get_object_or_404(models.Post, id=id)
    post_id.delete()
    return HttpResponse('Новость удалена!!! <a href = "/post_list/">На список новостей</a>')


def create_post_view(request):
    if request.method == 'POST':  # чтобы преобразовывал данные (картинки в файлы, текст просто)
        form = forms.PostForm(request.POST, request.FILES)
        if form.is_valid():  # валидация
            form.save()
            return HttpResponse('Данные успешно отправлены! <a href = "/post_list/">На список новостей</a>')
    else:
        form = forms.PostForm()
    return render(
        request,
        template_name='crud/create_post.html',
        context={
            'form': form
        }
    )


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
