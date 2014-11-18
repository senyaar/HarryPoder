from django.shortcuts import render, get_object_or_404
# from .models import Kitty
# from .forms import AddCat
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from friendmemeow.finder.forms import AddCat
from friendmemeow.finder.models import Kitty


def ready_cats(request):
    cats = Kitty.objects.filter(status__contains='Need').order_by('-posted_date')
    paginator = Paginator(cats, 9)

    page = request.GET.get('page')

    try:
        cat_list = paginator.page(page)
    except PageNotAnInteger:
        cat_list = paginator.page(1)
    except EmptyPage:
        cat_list = paginator.page(paginator.num_pages)
    return render(request, 'finder/ready_cats.html', {'cat_list': cat_list})


def cat_detail(request, pk):
    kitty = get_object_or_404(Kitty, pk=pk)
    return render(request, 'finder/cat_detail.html', {'kitty': kitty})

def add_cat(request):
    if request.method == "POST":
        form = AddCat(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('finder.views.cat_detail', pk=post.pk)
    else:
        form = AddCat()
    return render(request, 'finder/cat_edit.html', {'form': form})


def edit_cat(request, pk):
    post = get_object_or_404(Kitty, pk=pk)
    if request.method == "POST":
        form = AddCat(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('finder.views.cat_detail', pk=post.pk)
    else:
        form = AddCat(instance=post)
    return render(request, 'finder/cat_edit.html', {'form': form})
