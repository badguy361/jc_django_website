# Generated by Django 4.0.6 on 2022-08-08 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_alter_post_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='pic_url',
            field=models.ImageField(blank=True, upload_to='post_detail/'),
        ),
    ]
