from django.shortcuts import render, get_object_or_404, redirect
from .models import Kitty, Shelter
from .forms import AddCat
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
cats = Kitty.objects.filter(status__contains='Need').order_by('-posted_date')


def nine_cats_per_page(page):
    paginator = Paginator(cats, 9)

    try:
        cat_list = paginator.page(page)
    except PageNotAnInteger:
        cat_list = paginator.page(1)
    except EmptyPage:
        cat_list = paginator.page(paginator.num_pages)
    return cat_list


def half_age_plus_seven(age):
    return (age/2) + 7
