# Generated by Django 4.0.6 on 2022-08-23 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_homepage_en'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage_en',
            name='bottom_content',
            field=models.TextField(blank=True, max_length=400, verbose_name='底部內容'),
        ),
        migrations.AlterField(
            model_name='homepage_en',
            name='name',
            field=models.CharField(max_length=50, verbose_name='公司名稱'),
        ),
        migrations.AlterField(
            model_name='homepage_en',
            name='title',
            field=models.CharField(max_length=50, verbose_name='標題'),
        ),
        migrations.AlterField(
            model_name='homepage_en',
            name='title_content',
            field=models.TextField(max_length=400, verbose_name='標題內容'),
        ),
    ]
