# Generated by Django 4.2.6 on 2023-10-19 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='course_name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Q_name', models.CharField(max_length=150)),
                ('correct_ans', models.IntegerField()),
                ('option_1', models.CharField(max_length=50)),
                ('option_2', models.CharField(max_length=50)),
                ('option_3', models.CharField(max_length=50)),
                ('option_4', models.CharField(max_length=50)),
                ('course_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.course_name')),
            ],
        ),
        migrations.DeleteModel(
            name='HTML_AND_CSS_Q',
        ),
        migrations.DeleteModel(
            name='JAVA_Q',
        ),
        migrations.DeleteModel(
            name='JAVASCRIPT_Q',
        ),
        migrations.DeleteModel(
            name='PYTHON_Q',
        ),
    ]
