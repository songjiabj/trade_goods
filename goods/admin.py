from django.contrib import admin

# Register your models here.
from .models import Cat
from .models import L_cat
from .models import Goods_detail

admin.site.register(Cat)
admin.site.register(L_cat)
admin.site.register(Goods_detail)
