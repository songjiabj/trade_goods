from django.db import models
import django.utils.timezone
# Create your models here.

class Cat(models.Model):

    Detail_Cat = {
        ('digital', '数码产品'),
        ('book', '图书'),
        ('clothing', '服鞋包配饰'),
        ('instrument_toy', '乐器玩具'),
        ('toll', '配件设备工具'),
        ('vehicle_house', '车房'),
        ('other', '其他')
    }
    cat_id = models.CharField(max_length=4, primary_key=True)
    category = models.CharField(max_length=20, choices=Detail_Cat)

    def __str__(self):
        return self.category

    class Meta:
        db_table = 'cat'

class L_cat(models.Model):
    Large_Cat = (
        ('租', '租'),
        ('卖', '卖'),
        ('送', '送')
    )
    large_id = models.CharField(max_length=4, primary_key=True)
    large_category = models.CharField(max_length=10, choices=Large_Cat)

    def __str__(self):
        return self.large_category

    class Meta:
        db_table = 'l_cat'


class Goods_detail(models.Model):
    Detail_Cat = {
        ('c01', '数码产品'),
        ('c02', '图书'),
        ('c03', '服鞋包配饰'),
        ('c04', '乐器玩具'),
        ('c05', '配件设备工具'),
        ('c06', '车房'),
        ('c0', '其他')
    }
    Large_Cat = (
        ('b01', '租'),
        ('b02', '卖'),
        ('b03', '送')
    )
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=Detail_Cat)
    large_category = models.CharField(max_length=10, choices=Large_Cat)
    price = models.FloatField()
    phone = models.CharField(max_length=20)
    pub_date = models.DateTimeField(default=django.utils.timezone.now)
    address = models.CharField(max_length=100)
    img_1 = models.ImageField(default="C:/Users/acer/Pictures/001.jpg", upload_to="img_upload")
    img_2 = models.ImageField(default="C:/Users/acer/Pictures/001.jpg", upload_to="img_upload")
    img_3 = models.ImageField(default="C:/Users/acer/Pictures/001.jpg", upload_to="img_upload")
    coordinate_x = models.FloatField()
    coordinate_y = models.FloatField()

    class Meta:
        db_table = 'goods_detail'
