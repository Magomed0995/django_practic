from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Goods
from .forms import CategoryForms, GoodsForms
from django.http import HttpResponse

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'cars_store/category_list.html', {'categories': categories})

def create_category(request):
    if request.method == 'POST':
        form = CategoryForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForms()
        return render(request, 'cars_store/create_category.html', {'form': form})

def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    goods = Goods.objects.filter(category=category)
    return render(request, 'cars_store/category_detail.html', {'category': category, 'goods': goods})

def create_good(request, pk):
    if request.method == 'POST':
        form = GoodsForms(request.POST, request.FILES)
        category = get_object_or_404(Category, pk=pk)
        if form.is_valid():
            good = form.save(commit=False)
            good.category = category
            good.save()
            return redirect('category_detail', pk)
    else:
        form = GoodsForms()
        return render(request, 'cars_store/create_good.html', {'form': form})
    
def good_detail(request, c_pk, g_pk):
    good = get_object_or_404(Goods, pk=g_pk)
    return render(request, 'cars_store/good_detail.html', {'good': good, 'c_pk': c_pk})
