from django.db import models
from django.contrib.auth.models import User

from django_summernote.fields import SummernoteTextField #импорт поля для загрузки файлов

from django.urls import reverse



#модель ОБЪЯВЛЕНИЙ
# Объявления состоят из заголовка и текста, внутри которого могут быть картинки, встроенные видео и другой контент.
# Кроме того, пользователь обязательно должен определить объявление в одну из следующих категорий
class Post(models.Model): # объявления (посты), которые создают пользователи
    author = models.ForeignKey(User, on_delete=models.CASCADE)# связь «один ко многим» с моделью автора-создателя Author;
    title = models.CharField(max_length=128)  # заголовок статьи/новости;
    text = models.TextField(null=True, blank=True )  # текст объявления (поста)
    # dateCreation = models.DateTimeField(auto_now_add=True)  # автоматически добавляемая дата и время создания;
    CATEGORY_CHOICES = (
        ('Tanks', 'Танки'),
        ('Healers', 'Хилы'),
        ('DD', 'ДД'),
        ('Traders', 'Торговцы'),
        ('Guildmasters', 'Гилдмастеры'),
        ('Questgivers', 'Квестгиверы'),
        ('Blacksmiths', 'Кузнецы'),
        ('Leatherworkers', 'Кожевники'),
        ('Potions_Masters', 'Зельевары'),
        ('Spell_Masters', 'Мастеразаклинаний'))
    category = models.CharField(max_length=25, choices=CATEGORY_CHOICES, default='Tanks')  # поле с выбором категории;

    #когда потребуется где-то напечатать наш объект целиком:в панели администратора или в темплейте.
    #Вот как раз для вывода в HTML странице мы и указали, как должен выглядеть объект нашей модели.
    def __str__(self):
        return f"""{self.title}"""

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])


class Comment(models.Model):# Под каждым постом можно оставлять комментарии(отклик)
    comment_to_the_post = models.ForeignKey(Post, on_delete = models.CASCADE)# связь «один ко многим» с моделью Post;
    author_of_the_comment = models.ForeignKey(User, on_delete = models.CASCADE)# связь «один ко многим» со встроенной моделью User
    text_of_the_comment = models.TextField()# текст комментария;
    dateCreation_of_the_comment = models.DateTimeField(auto_now_add = True)# дата и время создания комментария;



# Create your models here.

# python manage.py makemigrations (создали миграцию для newapp)
# python manage.py migrate (применили миграцию для newapp)


