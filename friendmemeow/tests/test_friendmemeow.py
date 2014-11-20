import sys
import os
from mysite import settings
from mock import Mock, patch
import pytest
from finder.views import TestObj
from finder.models import Kitty


def test_it_doesnt_break():
    assert(True)

@pytest.mark.django_db
def test_get_all_kittys():
    allCats = Kitty.objects.filter(status__contains='Need')
    assert allCats is not None

# def test_can_add_cat():
#     request = Mock()
#     request.raw_post_data = "string"
#     request.method = "POST"
#     assert TestObj.add_cat(request).return_value is not None
#

