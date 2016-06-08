from django.shortcuts import get_object_or_404, render
from .models import Category

def index(request):
    category_list = Category.objects.all()
    return render(request, 'blog/index.html', {
     'category_list' : category_list
    })

def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'blog/category_detail.html', {
        'category' : category
    })
