# Generated by Django 2.0.7 on 2018-09-05 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0006_auto_20180904_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods_detail',
            name='img_1',
            field=models.ImageField(default='C:/Users/acer/Pictures/001.jpg', upload_to=''),
        ),
        migrations.AddField(
            model_name='goods_detail',
            name='img_2',
            field=models.ImageField(default='C:/Users/acer/Pictures/001.jpg', upload_to=''),
        ),
        migrations.AddField(
            model_name='goods_detail',
            name='img_3',
            field=models.ImageField(default='C:/Users/acer/Pictures/001.jpg', upload_to=''),
        ),
        migrations.AlterField(
            model_name='cat',
            name='category',
            field=models.CharField(choices=[('toll', '配件设备工具'), ('other', '其他'), ('clothing', '服鞋包配饰'), ('instrument_toy', '乐器玩具'), ('vehicle_house', '车房'), ('book', '图书'), ('digital', '数码产品')], max_length=20),
        ),
        migrations.AlterField(
            model_name='goods_detail',
            name='category',
            field=models.CharField(choices=[('c03', '服鞋包配饰'), ('c04', '乐器玩具'), ('c02', '图书'), ('c0', '其他'), ('c01', '数码产品'), ('c05', '配件设备工具'), ('c06', '车房')], max_length=20),
        ),
    ]
