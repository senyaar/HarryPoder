from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse

from rest_framework import generics, permissions, viewsets
from .models import Kitty, Shelter
from .serializers import KittySerializer, ShelterSerializer

from .forms import AddCat
from .functions import half_age_plus_seven, nine_cats_per_page, monthly_food_cost


# def ready_cats(request):
#     page = request.GET.get('page')
#     cat_list = nine_cats_per_page(page)
#     return render(request, 'finder/ready_cats.html', {'cat_list': cat_list})
#
#
# def cat_detail(request, pk):
#     kitty = get_object_or_404(Kitty, pk=pk)
#     age7 = half_age_plus_seven(kitty.age)
#     food_cost =  monthly_food_cost(kitty.weight)
#     return render(request, 'finder/cat_detail.html', {'kitty': kitty, 'age7': age7, 'food_cost': food_cost})
#
#
# def cat_form(request, pk=None):
#     if pk is not None:
#         catID = get_object_or_404(Kitty, pk=pk)
#     else:
#         catID = Kitty()
#
#     if request.method == "POST":
#         form = AddCat(request.POST, request.FILES, instance=catID)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.save()
#             return redirect('finder.views.cat_detail', pk=post.pk)
#     else:
#         form = AddCat(instance=catID)
#     return render_to_response('finder/cat_edit.html', {'form': form}, context_instance=RequestContext(request))


class CatList(viewsets.ModelViewSet):
    queryset = Kitty.objects.all()
    serializer_class = KittySerializer


class CatDetail(generics.RetrieveAPIView):
    model = Kitty
    serializer_class = KittySerializer
    lookup_field = 'id'


class ShelterList(viewsets.ModelViewSet):
    queryset = Shelter.objects.all()
    serializer_class = ShelterSerializer
