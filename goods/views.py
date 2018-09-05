from django.shortcuts import render
# Create your views here.
from .models import Goods_detail
from .models import Cat
from .models import L_cat
from django.views import generic
from django import forms


def map(request):
    if request.method == 'POST':
        title = request.POST.get("title", None)
        description = request.POST.get("description", None)
        category = request.POST.get("category", None)
        large_category = request.POST.get("large_category", None)
        price = request.POST.get("price", None)
        phone = request.POST.get("phone", None)
        address = request.POST.get("address", None)
        coordinate_x = request.POST.get("coordinate_x", None)
        coordinate_y = request.POST.get("coordinate_y", None)
        q = Cat.objects.get(category=category)
        l = L_cat.objects.get(large_category=large_category)
        file1 = request.FILES.get('img_1', None)
        file2 = request.FILES.get('img_2', None)
        file3 = request.FILES.get('img_3', None)

        if file1 and file2 and file3:
            img_1 = request.FILES['img_1']
            img_2 = request.FILES["img_2"]
            img_3 = request.FILES["img_3"]
            good = Goods_detail(title=title, description=description, category=q.cat_id, large_category=l.large_id,
                                price=price, phone=phone, address=address, img_1=img_1, img_2=img_2, img_3=img_3,
                                coordinate_x=coordinate_x, coordinate_y=coordinate_y)
        elif file1 and file2:
            img_1 = request.FILES['img_1']
            img_2 = request.FILES["img_2"]
            good = Goods_detail(title=title, description=description, category=q.cat_id, large_category=l.large_id,
                                price=price, phone=phone, address=address, img_1=img_1, img_2=img_2,
                                coordinate_x=coordinate_x, coordinate_y=coordinate_y)
        elif file1:
            img_1 = request.FILES['img_1']
            good = Goods_detail(title=title, description=description, category=q.cat_id, large_category=l.large_id,
                                price=price, phone=phone, address=address, img_1=img_1,
                                coordinate_x=coordinate_x, coordinate_y=coordinate_y)
        else:
            good = Goods_detail(title=title, description=description, category=q.cat_id, large_category=l.large_id,
                                price=price, phone=phone, address=address,
                                coordinate_x=coordinate_x, coordinate_y=coordinate_y)
        good.save()

    latest_good_list = Goods_detail.objects.order_by('-pub_date')[:5]
    context = {'latest_good_list': latest_good_list}
    return render(request, 'goods/map.html', context)


def mapC00(request):
    latest_good_list = Goods_detail.objects.order_by('-pub_date')[:5]
    context = {'latest_good_list': latest_good_list, 'cat_text': "all_1"}
    return render(request,'goods/map/c01.html', context)

def mapB00(request):
    latest_good_list = Goods_detail.objects.order_by('-pub_date')[:5]
    context = {'latest_good_list': latest_good_list, 'cat_text': "all_2"}
    return render(request,'goods/map/c01.html', context)

def mapCorB(request, category):
    latest_good_list = Goods_detail.objects.filter(category=category)
    context = {'latest_good_list': latest_good_list, 'cat_text': category}
    return render(request,'goods/map/c01.html', context)

def mapCB(request, category, l_category):
    if category=="c00":
        latest_good_list = Goods_detail.objects.filter(
            large_category=l_category
        );
    elif category=="b00":
        latest_good_list = Goods_detail.objects.filter(
            category=category
        );
    else:
        latest_good_list = Goods_detail.objects.filter(
            category=category
        ).filter(
            large_category=l_category
        );
    context = {'latest_good_list': latest_good_list, 'cat_text': {"cat": category, "l_cat": l_category}}
    return render(request, 'goods/map/c01.html', context)


def home(request):
    return render(request,'goods/home.html')

def product(request):
    return render(request,'goods/product.html')

class DetailView(generic.DetailView):
    model = Goods_detail
    template_name = 'goods/detail.html'

