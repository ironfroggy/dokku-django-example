from django.shortcuts import render

from count.models import Count


def count(request, template_name='count/count.html'):
    c = Count.objects.get_or_create(pk=1)[0]
    return render(request, template_name, {
        'count': c.last_number,
    })
