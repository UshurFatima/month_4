# Generated by Django 5.1 on 2024-09-11 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_post_email_news_remove_post_url_news_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='like_or_dislike',
            field=models.CharField(choices=[('👍', '👍'), ('👎', '👎')], max_length=200, null=True),
        ),
    ]
