from django.views.generic.edit import CreateView

from littlebro.models import PoliceOfficer

from generic import ModelCreate, ModelList, ModelDetail


class PoliceOfficerCreate(ModelCreate):
    model = PoliceOfficer


class PoliceOfficerList(ModelList):
    model = PoliceOfficer


class PoliceOfficerDetail(ModelDetail):
    model = PoliceOfficer
