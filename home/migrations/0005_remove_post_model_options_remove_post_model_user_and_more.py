# Generated by Django 4.2.6 on 2023-10-19 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_post_model_quizzes_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post_model',
            name='options',
        ),
        migrations.RemoveField(
            model_name='post_model',
            name='user',
        ),
        migrations.RemoveField(
            model_name='question',
            name='course_name',
        ),
        migrations.DeleteModel(
            name='Option',
        ),
        migrations.DeleteModel(
            name='post_model',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
