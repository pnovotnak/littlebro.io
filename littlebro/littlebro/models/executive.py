from django.db import models
from django.contrib.contenttypes import generic

from generic import Official


class PoliceOfficer(Official):
    """
    An officer of the law
    """
    badge_number = models.IntegerField()
