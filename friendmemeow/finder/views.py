from django.shortcuts import render, get_object_or_404
# from .models import Kitty
# from .forms import AddCat
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from finder.forms import AddCat
from finder.models import Kitty
from finder.functions import half_age_plus_seven, nineCatsPerPage


def ready_cats(request):
    page = request.GET.get('page')
    cat_list = nineCatsPerPage(page)
    return render(request, 'finder/ready_cats.html', {'cat_list': cat_list})


def cat_detail(request, pk):
    kitty = get_object_or_404(Kitty, pk=pk)
    age7 = half_age_plus_seven(kitty.age)
    return render(request, 'finder/cat_detail.html', {'kitty': kitty, 'age7': age7})


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
