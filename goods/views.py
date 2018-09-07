from django.shortcuts import render
# Create your views here.
from .models import Goods_detail
from .models import Cat
from .models import L_cat
from django.views import generic
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def map(request):
    if request.method == 'POST':
        upload_good(request)
    latest_good_list = Goods_detail.objects.order_by('-pub_date')
    paginator = Paginator(latest_good_list, 5)

    page = request.GET.get('page', 1)
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'goods/map.html', {"contacts": contacts})

def upload_good(request):
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
    good = Goods_detail(title=title, description=description, category=q.cat_id, large_category=l.large_id,
                        price=price,
                        phone=phone, address=address, coordinate_x=coordinate_x, coordinate_y=coordinate_y)

    if file1:
        img_1 = request.FILES['img_1']
        good.img_1 = img_1
    if file2:
        img_2 = request.FILES["img_2"]
        good.img_2 = img_2
    if file3:
        img_3 = request.FILES["img_3"]
        good.img_3 = img_3
    good.save()

def mapCorB(request, category):
    if request.method == 'POST':
        return map(request)
    else:
        latest_good_list = Goods_detail.objects.filter(Q(category=category) | Q(large_category=category))
        paginator = Paginator(latest_good_list, 5)
        page = request.GET.get('page', 1)
        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            contacts = paginator(1)
        except EmptyPage:
            contacts = paginator.page(paginator.num_pages)

        context = {"contacts": contacts, 'cat_text': category}
        return render(request, 'goods/map/c01.html', context)

def mapCB(request, category, l_category):
    if request.method == 'POST':
        return map(request)
    else:
        latest_good_list = Goods_detail.objects.filter(
            category=category
        ).filter(
            large_category=l_category
        )
        paginator = Paginator(latest_good_list, 5)
        page = request.GET.get('page', 1)
        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            contacts = paginator(1)
        except EmptyPage:
            contacts = paginator.page(paginator.num_pages)

        context = {"contacts": contacts, 'cat_text': {"cat": category, "l_cat": l_category}}
        return render(request, 'goods/map/c01.html', context)

def productCorB(request, category):
    if request.method == 'POST':
        return map(request)
    else:
        latest_good_list = Goods_detail.objects.filter(Q(category=category) | Q(large_category=category))
        paginator = Paginator(latest_good_list, 5)
        page = request.GET.get('page', 1)
        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            contacts = paginator(1)
        except EmptyPage:
            contacts = paginator.page(paginator.num_pages)

        context = {"contacts": contacts, 'cat_text': category}
        return render(request, 'goods/map/p01.html', context)

def productCB(request, category, l_category):
    if request.method == 'POST':
        return map(request)
    else:
        latest_good_list = Goods_detail.objects.filter(
            category=category
        ).filter(
            large_category=l_category
        )
        paginator = Paginator(latest_good_list, 5)
        page = request.GET.get('page', 1)
        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            contacts = paginator(1)
        except EmptyPage:
            contacts = paginator.page(paginator.num_pages)

        context = {"contacts": contacts, 'cat_text': {"cat": category, "l_cat": l_category}}
        return render(request, 'goods/map/p01.html', context)

def home(request):
    return render(request,'goods/home.html')

def product(request):
    if request.method == 'GET':
        search = request.GET.get("search", None)
        if search:
            latest_good_list = Goods_detail.objects.filter(Q(title=search) | Q(description=search))
            paginator = Paginator(latest_good_list, 20)

            page = request.GET.get('page', 1)
            try:
                contacts = paginator.page(page)
            except PageNotAnInteger:
                contacts = paginator(1)
            except EmptyPage:
                contacts = paginator.page(paginator.num_pages)
        else:
            latest_good_list = Goods_detail.objects.order_by('-pub_date')
            paginator = Paginator(latest_good_list, 20)

            page = request.GET.get('page', 1)
            try:
                contacts = paginator.page(page)
            except PageNotAnInteger:
                contacts = paginator(1)
            except EmptyPage:
                contacts = paginator.page(paginator.num_pages)
    else:
        latest_good_list = Goods_detail.objects.order_by('-pub_date')
        paginator = Paginator(latest_good_list, 20)

        page = request.GET.get('page', 1)
        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            contacts = paginator(1)
        except EmptyPage:
            contacts = paginator.page(paginator.num_pages)

    return render(request, 'goods/product.html', {"contacts": contacts})



class DetailView(generic.DetailView):
    model = Goods_detail
    template_name = 'goods/detail.html'

