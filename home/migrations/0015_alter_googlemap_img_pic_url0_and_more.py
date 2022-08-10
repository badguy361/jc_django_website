# Generated by Django 4.0.6 on 2022-08-08 12:34

from django.db import migrations, models
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_alter_homepage_pic_url1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='googlemap_img',
            name='pic_url0',
            field=models.ImageField(blank=True, storage=home.models.OverwriteStorage(), upload_to='home_image/google_map_img', verbose_name='子標題圖片10 URL'),
        ),
        migrations.AlterField(
            model_name='googlemap_img',
            name='pic_url1',
            field=models.ImageField(blank=True, storage=home.models.OverwriteStorage(), upload_to='home_image/google_map_img', verbose_name='子標題圖片1 URL'),
        ),
        migrations.AlterField(
            model_name='googlemap_img',
            name='pic_url2',
            field=models.ImageField(blank=True, storage=home.models.OverwriteStorage(), upload_to='home_image/google_map_img', verbose_name='子標題圖片2 URL'),
        ),
        migrations.AlterField(
            model_name='googlemap_img',
            name='pic_url3',
            field=models.ImageField(blank=True, storage=home.models.OverwriteStorage(), upload_to='home_image/google_map_img', verbose_name='子標題圖片3 URL'),
        ),
        migrations.AlterField(
            model_name='googlemap_img',
            name='pic_url4',
            field=models.ImageField(blank=True, storage=home.models.OverwriteStorage(), upload_to='home_image/google_map_img', verbose_name='子標題圖片4 URL'),
        ),
        migrations.AlterField(
            model_name='googlemap_img',
            name='pic_url5',
            field=models.ImageField(blank=True, storage=home.models.OverwriteStorage(), upload_to='home_image/google_map_img', verbose_name='子標題圖片5 URL'),
        ),
        migrations.AlterField(
            model_name='googlemap_img',
            name='pic_url6',
            field=models.ImageField(blank=True, storage=home.models.OverwriteStorage(), upload_to='home_image/google_map_img', verbose_name='子標題圖片6 URL'),
        ),
        migrations.AlterField(
            model_name='googlemap_img',
            name='pic_url7',
            field=models.ImageField(blank=True, storage=home.models.OverwriteStorage(), upload_to='home_image/google_map_img', verbose_name='子標題圖片7 URL'),
        ),
        migrations.AlterField(
            model_name='googlemap_img',
            name='pic_url8',
            field=models.ImageField(blank=True, storage=home.models.OverwriteStorage(), upload_to='home_image/google_map_img', verbose_name='子標題圖片8 URL'),
        ),
        migrations.AlterField(
            model_name='googlemap_img',
            name='pic_url9',
            field=models.ImageField(blank=True, storage=home.models.OverwriteStorage(), upload_to='home_image/google_map_img', verbose_name='子標題圖片9 URL'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='big_pic_url1',
            field=models.ImageField(blank=True, storage=home.models.OverwriteStorage(), upload_to='home_image/', verbose_name='圖片1 URL'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='big_pic_url2',
            field=models.ImageField(blank=True, storage=home.models.OverwriteStorage(), upload_to='home_image/', verbose_name='圖片2 URL'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='big_pic_url3',
            field=models.ImageField(blank=True, storage=home.models.OverwriteStorage(), upload_to='home_image/', verbose_name='圖片3 URL'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='pic_url2',
            field=models.ImageField(blank=True, storage=home.models.OverwriteStorage(), upload_to='home_image/', verbose_name='子標題圖片2 URL'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='pic_url3',
            field=models.ImageField(blank=True, storage=home.models.OverwriteStorage(), upload_to='home_image/', verbose_name='子標題圖片3 URL'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='pic_url4',
            field=models.ImageField(blank=True, storage=home.models.OverwriteStorage(), upload_to='home_image/', verbose_name='子標題圖片4 URL'),
        ),
    ]
