import sys
import os
from mysite import settings
from mock import Mock, patch
import pytest
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from finder.functions import half_age_plus_seven
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



