import sys
import os
import factory
import unittest
from django.core.urlresolvers import resolve

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from finder.functions import half_age_plus_seven, monthly_food_cost
from finder.models import Kitty
from finder.views import ready_cats, cat_detail


class KittyFactory(factory.Factory):
    class Meta:
        model = Kitty
    name='meesh'
    gender='F'
    age=20
    weight=5

class KittyTestCase(unittest.TestCase):

    def setUp(self):
        self.cat = KittyFactory()

    def test_add_7(self):
        age7 = half_age_plus_seven(self.cat.age)
        self.assertEqual(age7, 17)

    def test_monthly_food_cost(self):
        food_cost = monthly_food_cost(self.cat.weight)
        self.assertEqual(round(food_cost, 2), 11.57)

    def test_root_url_resolve_to_ready_cats_view(self):
        found = resolve('/')
        self.assertEqual(found.func, ready_cats)

    def test_kitty_url_resolve_to_cat_detail_view(self):
        found = resolve('/kitty/1/')
        self.assertEqual(found.func, cat_detail)


