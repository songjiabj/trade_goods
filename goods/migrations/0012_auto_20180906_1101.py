# Generated by Django 2.0.7 on 2018-09-06 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0011_auto_20180905_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='category',
            field=models.CharField(choices=[('toll', '配件设备工具'), ('instrument_toy', '乐器玩具'), ('other', '其他'), ('vehicle_house', '车房'), ('clothing', '服鞋包配饰'), ('book', '图书'), ('digital', '数码产品')], max_length=20),
        ),
        migrations.AlterField(
            model_name='goods_detail',
            name='category',
            field=models.CharField(choices=[('c0', '其他'), ('c05', '配件设备工具'), ('c02', '图书'), ('c01', '数码产品'), ('c03', '服鞋包配饰'), ('c04', '乐器玩具'), ('c06', '车房')], max_length=20),
        ),
        migrations.AlterField(
            model_name='goods_detail',
            name='img_1',
            field=models.ImageField(default='001.png', upload_to='img_upload'),
        ),
        migrations.AlterField(
            model_name='goods_detail',
            name='img_2',
            field=models.ImageField(default='001.png', upload_to='img_upload'),
        ),
        migrations.AlterField(
            model_name='goods_detail',
            name='img_3',
            field=models.ImageField(default='001.png', upload_to='img_upload'),
        ),
    ]