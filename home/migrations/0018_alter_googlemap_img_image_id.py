# Generated by Django 4.0.6 on 2022-08-08 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_alter_googlemap_img_pic_url0_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='googlemap_img',
            name='image_ID',
            field=models.TextField(editable=False, primary_key=True, serialize=False, verbose_name='圖片群ID'),
        ),
    ]
