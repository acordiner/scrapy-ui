# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task


@shared_task
def scrapyd_schedule(project, spider):
    # call the scrapyd schedule.json API function:
    # http://scrapyd.readthedocs.io/en/stable/api.html#schedule-json
    print("curl http://localhost:6800/schedule.json -d project=%s -d spider=%s" % (project, spider))
