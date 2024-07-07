from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy

# Импортируем класс, который говорит нам о том,
# что в этом представлении мы будем выводить список объектов из БД
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post
from datetime import datetime
from .forms import PostForm
from django.utils import timezone

# СПИСОК ОБЪЯВЛЕНИЙ
class PostList(ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = Post
    # # Поле, которое будет использоваться для сортировки объектов
    # ordering = 'dateCreation'
    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'posts.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'posts'

# ОДНО КОНКРЕТНОЕ ОБЪЯВЛЕНИЕ
class PostDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельному товару
    model = Post
    # Используем другой шаблон — product.html
    template_name = 'post_detail.html'
    # Название объекта, в котором будет выбранный пользователем продукт
    context_object_name = 'post_detail'
    def get_context_data(self, **kwargs):
        # С помощью super() мы обращаемся к родительским классам
        # и вызываем у них метод get_context_data с теми же аргументами,
        # что и были переданы нам.
        # В ответе мы должны получить словарь.
        context = super().get_context_data(**kwargs)
        # К словарю добавим текущую дату в ключ 'time_now'.
        context['time_now'] = datetime.utcnow()
        return context

# СОЗДАНИЕ ПОСТА АВТОРИЗИРОВАННЫМИ ПОЛЬЗОВАТЕЛЯМИ
class PostCreate(PermissionRequiredMixin,CreateView):
    permission_required = ('callboard_app.add_post',) #add_post из админки Chosen permissions
    form_class = PostForm # Указываем нашу разработанную форму
    model = Post # модель
    template_name = 'post_create.html' #новый шаблон, в котором используется форма.

# РЕДАКТИРОВАНИЕ ПОСТА АВТОРИЗИРОВАННЫМИ ПОЛЬЗОВАТЕЛЯМИ
class PostUpdate(PermissionRequiredMixin, UpdateView):# Добавляем новое представление для создания новости.
    permission_required = ('callboard_app.change_post',)
    form_class = PostForm # Указываем нашу разработанную форму
    model = Post # модель
    template_name = 'post_update.html' # и новый шаблон, в котором используется форма.
    success_url = reverse_lazy('posts')  # куда перенеправить поль-ля после удаления товара