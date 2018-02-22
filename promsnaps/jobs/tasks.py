from __future__ import absolute_import, unicode_literals
import logging
from promsnaps.jobs.runner import app
from promsnaps.jobs.job_base import JobBase

logger = logging.getLogger(__name__)


@app.task(bind=True, base=JobBase)
def concat(self, a, b):
    """ test job """
    logger.info("Run test job")
    return a + b


def test_job():
    assert concat.delay(3, 5).get() == 8
