# Generated by Django 4.0.6 on 2022-08-23 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0005_aboutcontent_en_member_en'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutcontent_en',
            name='content',
            field=models.TextField(blank=True, max_length=1500, verbose_name='內容'),
        ),
    ]
