import sys
import os
import pytest
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from finder.functions import half_age_plus_seven, monthly_food_cost
from finder.models import Kitty


def test_it_doesnt_break():
    assert(True)


@pytest.mark.django_db
def test_get_all_kittys():
    allCats = Kitty.objects.filter(status__contains='Need')
    assert allCats is not None


def test_add_7():
    age = 20
    age7 = half_age_plus_seven(age)
    assert age7 == 17

def test_monthly_food_cost():
    weight = 5
    food_cost = monthly_food_cost(weight)
    assert round(food_cost, 2) == 11.57



