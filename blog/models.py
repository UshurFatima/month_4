from django.db import models


# создание новой таблицы, обязательно наследуемся от models.Model
class Post(models.Model):
    # прописываем обязательно два раза, так как один идет
    # в таблицу, а второй отображается
    LIKE_OR_DISLIKE = (
        ('👍', '👍'),
        ('👎', '👎'),

    )

    #       типы данных как в sqlite, здесь - varchar
    title = models.CharField(max_length=255,  # verbose_name - сообщение при
                             verbose_name='Enter a title', db_index=True, null=True)  # добавлении названия
    # в скобках blank=True - поле может быть пустым, если ничего не пишем -
    # поле должно заполняться
    # null=True, чтобы переделать миграцию
    image = models.ImageField(upload_to='post/',  # все изображения будут сохраняться
                              # в медиа (из-за настроек) в папку пост
                              verbose_name='download picture', null=True)
    description = models.TextField(verbose_name='write the text', null=True)
    news_url = models.URLField(verbose_name='write the url of news origin', null=True)
    news_email = models.EmailField(verbose_name='write a contact email address', null=True)
    like_or_dislike = models.CharField(max_length=200, choices=LIKE_OR_DISLIKE, null=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, null=True)  # чтобы время бралось из настроек

    # для админа
    def __str__(self):
        return f'{self.title} - {self.created_at}'


class Review(models.Model):  # foreignkey - один к многим
    post_review = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='review_post')
    # каскад - когда удаляют пост пропадают и отзывы
    # related_name - ключ к данным (как context)
    text_post = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.text_post} - {self.created_at}'