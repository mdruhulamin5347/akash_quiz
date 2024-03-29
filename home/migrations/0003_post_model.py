# Generated by Django 4.2.6 on 2023-10-19 18:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0002_course_name_question_delete_html_and_css_q_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='post_model',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('create_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('quizzes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
