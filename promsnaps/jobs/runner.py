from __future__ import absolute_import, unicode_literals
import celery

app = celery.Celery('promsnaps', include=['promsnaps.jobs.tasks'])
app.config_from_object('promsnaps.jobs.celeryconfig')
# update_conf = {}
# Optional configuration, see the application user guide.
# app.conf.update(**update_conf)

if __name__ == '__main__':
    app.start()
