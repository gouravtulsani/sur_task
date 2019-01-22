from django.shortcuts import render
from .models import AdultData
from django.http import JsonResponse, HttpResponse
from django.db.models import Count
import csv
from django.core.cache import cache

# Create your views here.
def home(request):
    resp_1 = sex_destribution(request)
    print(resp_1)
    resp_2 = relation_destribution(request)
    return render(request, 'index.html', {'chart1_data': resp_1, 'chart2_data': resp_2})


def sex_destribution(request):
    data = AdultData.objects.values('sex').annotate(count=Count('sex'))
    resp = {'result': list(data)}
    return JsonResponse(resp)


def relation_destribution(request):
    data = AdultData.objects.values('relationship').annotate(
        count=Count('relationship'))
    resp = {'result': list(data)}
    return JsonResponse(resp)


def raw_data(request):
    response = HttpResponse(content_type='text/csv')
    cache_key = 'raw_data'
    cache_time = 3600
    keys = [field.attname for field in AdultData._meta.fields]
    del keys[0]

    data = cache.get(cache_key)

    if not data:
        print('db lookup..')
        data = AdultData.objects.values_list(*keys)

    cache.set(cache_key, data, cache_time)

    writer = csv.writer(response)
    writer.writerow(keys)
    writer.writerows(data)

    return response
