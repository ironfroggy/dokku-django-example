from __future__ import absolute_import
import logging
from celery import shared_task
from celery.task import periodic_task
from datetime import timedelta
from .models import Count

#logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('tasks_info')

logger.info(' * tasks')


@periodic_task(run_every=timedelta(seconds=10))
def print_count():
    c = Count.objects.get_or_create(pk=1)[0]
    logger.info('count: %d' % (c.last_number, ))
    c.last_number += 1
    c.save()
