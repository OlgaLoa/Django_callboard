# Generated by Django 4.2.13 on 2024-06-15 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('callboard_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='dateCreation',
            new_name='dateCreation_of_the_comment',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='commentPost',
            new_name='post_comment',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='text',
            new_name='text_of_the_comment',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='commentUser',
            new_name='user_of_the_comment',
        ),
    ]
