# Generated by Django 4.0.6 on 2022-07-29 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='標題')),
                ('content', models.CharField(max_length=200, verbose_name='內容')),
            ],
        ),
    ]
