# Generated by Django 4.2.13 on 2024-06-17 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('callboard_app', '0003_remove_post_post_category_post_category_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='user_of_the_comment',
            new_name='author_of_the_comment',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='post_comment',
            new_name='comment_to_the_post',
        ),
    ]