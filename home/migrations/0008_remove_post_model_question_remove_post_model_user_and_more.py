# Generated by Django 4.2.6 on 2023-10-21 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_post_model'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post_model',
            name='question',
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
            name='course_name',
        ),
        migrations.DeleteModel(
            name='post_model',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
