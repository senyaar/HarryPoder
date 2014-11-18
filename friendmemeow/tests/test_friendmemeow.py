import sys
import os
from mock import Mock, patch
import pytest
from finder.views import ready_cats
from finder.models import Kitty


def test_it_doesnt_break():
    assert(True)

@pytest.mark.django_db
def test_get_all_kittys():
    allCats = Kitty.objects.filter(status__contains='Need')
    assert allCats == None
