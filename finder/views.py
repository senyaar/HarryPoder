from django.shortcuts import render, get_object_or_404
from .models import Kitty
from .forms import AddCat
from django.core.urlresolvers import reverse
from django.shortcuts import redirect


def ready_cats(request):
	cats = Kitty.objects.filter(status__contains='Need').order_by('-posted_date')
	return render(request, 'finder/ready_cats.html', {'cats': cats})

def cat_detail(request, pk):
    kitty = get_object_or_404(Kitty, pk=pk)
    return render(request, 'finder/cat_detail.html', {'kitty': kitty})


def add_cat(request):
    if request.method == "POST":
        form = AddCat(request.POST)
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
        form = AddCat(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('finder.views.cat_detail', pk=post.pk)
    else:
        form = AddCat(instance=post)
    return render(request, 'finder/cat_edit.html', {'form': form})