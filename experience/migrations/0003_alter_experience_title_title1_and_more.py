# Generated by Django 4.0.6 on 2022-10-11 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experience', '0002_alter_experience_title_en_title1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience_title',
            name='title1',
            field=models.CharField(blank=True, max_length=50, verbose_name='主題名稱1'),
        ),
        migrations.AlterField(
            model_name='experience_title',
            name='title2',
            field=models.CharField(blank=True, max_length=50, verbose_name='主題名稱2'),
        ),
    ]
