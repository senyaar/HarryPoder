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


def monthly_food_cost(weight):
    daily_calories = 30 * weight
    cup_calories = 300
    daily_cups = daily_calories/cup_calories
    cups_per_bag = 20.74
    bag_cost = 16
    return (daily_cups*30)/cups_per_bag * 16


