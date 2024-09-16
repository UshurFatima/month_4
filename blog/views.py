from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from . import models, forms


class SearchView(generic.ListView):
    template_name = 'post_list.html'
    context_object_name = 'post_object'
    paginate_by = 5  # чтоб делились по страницам

    def get_queryset(self):                      # для поиска по символам;      то, что мы вводим в поиск
        return models.Post.objects.filter(title__icontains=self.request.GET.get('q')).order_by('-id')

    def get_context_data(self, *, object_list=None, **kwargs):  # получаем данные из базы
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context


class PostUpdateListView(generic.ListView):
    template_name = 'crud/post_list_edit.html'
    context_object_name = 'post_object'
    model = models.Post

    def get_queryset(self):
        return self.model.objects.all(). order_by('-id')


class PostEditView(generic.UpdateView):
    template_name = 'crud/update_post.html'
    form_class = forms.PostForm
    success_url = '/post_list_edit/'

    def get_object(self, **kwargs):
        post_id = self.kwargs.get('id')
        return get_object_or_404(models.Post, id=post_id)


# def post_list_edit_view(request):
#     if request.method == "GET":  # проверка на запрос
#         # query запрос
#         post_object = models.Post.objects.all()  # выводит все объекты из таблицы Пост
#         return render(
#             request,
#             template_name='crud/post_list_edit.html',
#             context={
#                 'post_object': post_object
#             }
#         )


# def update_post_view(request, id):
#     post_id = get_object_or_404(models.Post, id=id)
#     if request.method == 'POST':
#         form = forms.PostForm(request.POST, instance=post_id)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Новость отредактирована!!! <a href = "/post_list/">На список новостей</a>')
#     else:
#         form = forms.PostForm(instance=post_id)
#
#     return render(
#         request,
#         template_name='crud/update_post.html',
#         context={
#             'form': form,
#             'post_id': post_id
#         }
#     )


class PostListDeleteView(generic.ListView):
    template_name = 'crud/post_list_delete.html'
    context_object_name = 'post_object'
    model = models.Post

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')


class PostDropDeleteView(generic.DeleteView):
    template_name = 'crud/confirm_delete.html'
    success_url = '/post_list_delete/'

    def get_object(self, **kwargs):
        post_id = self.kwargs.get('id')
        return get_object_or_404(models.Post, id=post_id)


# def post_list_delete_view(request):
#     if request.method == "GET":  # проверка на запрос
#         # query запрос
#         post_object = models.Post.objects.all()  # выводит все объекты из таблицы Пост
#         return render(
#             request,
#             template_name='crud/post_list_delete.html',
#             context={
#                 'post_object': post_object
#             }
#         )


# def post_drop_view(request, id):
#     post_id = get_object_or_404(models.Post, id=id)
#     post_id.delete()
#     return HttpResponse('Новость удалена!!! <a href = "/post_list/">На список новостей</a>')


class PostCreateView(generic.CreateView):
    template_name = 'crud/create_post.html'
    form_class = forms.PostForm
    success_url = '/post_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(PostCreateView, self).form_valid(form=form)


# def create_post_view(request):
#     if request.method == 'POST':  # чтобы преобразовывал данные (картинки в файлы, текст просто)
#         form = forms.PostForm(request.POST, request.FILES)
#         if form.is_valid():  # валидация
#             form.save()
#             return HttpResponse('Данные успешно отправлены! <a href = "/post_list/">На список новостей</a>')
#     else:
#         form = forms.PostForm()
#     return render(
#         request,
#         template_name='crud/create_post.html',
#         context={
#             'form': form
#         }
#     )


# для полной информации
class PostDetailView(generic.DetailView):
    template_name = 'post_detail.html'
    context_object_name = 'post_id'

    def get_object(self, **kwargs):
        post_id = self.kwargs.get('id')
        return get_object_or_404(models.Post, id=post_id)


# def post_detail_view(request, id):
#     if request.method == "GET":
#         post_id = get_object_or_404(models.Post, id=id)
#         return render(
#             request,
#             template_name='post_detail.html',
#             context={
#                 'post_id': post_id
#             }
#         )


# вывод неполной информации
class PostListView(generic.ListView):
    template_name = 'post_list.html'
    context_object_name = 'post_object'
    model = models.Post

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')


# def post_list_view(request):
#     два запроса: пост и гет; пост - приватные данные/когда пишем и
#     отправляем в бд, гет - выводим информацию
#     if request.method == "GET":  # проверка на запрос
#         query запрос
#         post_object = models.Post.objects.all()  # выводит все объекты из таблицы Пост
#         return render(
#             request,
#             template_name='post_list.html',
#             context={
#                 'post_object': post_object
#             }
#         )


def hello_view(request):
    return HttpResponse('hello world!!!')
