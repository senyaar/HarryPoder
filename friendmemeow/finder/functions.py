from finder.models import Kitty, Shelter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

cats = Kitty.objects.filter(status__contains='Need').order_by('-posted_date')


def nineCatsPerPage(page):
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