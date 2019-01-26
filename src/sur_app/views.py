from .models import AdultData
from django.http import JsonResponse
from django.db.models import Count
from django.core.cache import cache

# Create your views here.
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
    cache_key = 'raw_data'
    cache_time = 3600
    keys = [field.attname for field in AdultData._meta.fields]
    del keys[0]

    data = cache.get(cache_key)

    if not data:
        print('db lookup..')
        data = AdultData.objects.values_list(*keys)[:10]
    
    cache.set(cache_key, data, cache_time)

    resp = {'result': list(data)}
    resp['keys'] = keys
    return JsonResponse(resp)
