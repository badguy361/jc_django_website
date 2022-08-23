# Generated by Django 4.0.6 on 2022-08-23 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0008_mappage'),
    ]

    operations = [
        migrations.CreateModel(
            name='MapPage_EN',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='公司名稱')),
                ('bottom_title', models.CharField(blank=True, max_length=50, verbose_name='底部標題')),
                ('bottom_content', models.TextField(blank=True, max_length=400, verbose_name='底部內容')),
                ('bottom_email', models.CharField(blank=True, max_length=100, verbose_name='底部email')),
                ('bottom_phone', models.CharField(blank=True, max_length=50, verbose_name='底部連絡電話')),
            ],
        ),
    ]
