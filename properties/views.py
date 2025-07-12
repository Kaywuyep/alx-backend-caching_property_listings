from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from .models import Property
from .utils import get_all_properties

# this is for test on a UI
# @cache_page(60 * 15)  # Cache for 15 minutes
# def property_list(request):
#     properties = Property.objects.all()
#     return render(
#         request,
#         'properties/property_list.html',
#         {'properties': properties})


@cache_page(60 * 15)  # Cache for 15 minutes
def property_list(request):
    properties = get_all_properties()
    # properties = Property.objects.all().values(
    #     'id', 'title', 'description', 'price', 'location', 'created_at'
    # )
    return JsonResponse({
        "data": properties
        # "data": list(properties)
    })
