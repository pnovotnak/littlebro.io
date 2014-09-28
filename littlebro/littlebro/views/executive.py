from django.views.generic.edit import CreateView

from littlebro.models import Police

from generic import ModelCreate, ModelList, ModelDetail


class PoliceMixin(object):
    model = Police


class PoliceOfficerCreate(ModelCreate, PoliceMixin):
    pass


class PoliceOfficerList(ModelList, PoliceMixin):
    pass


class PoliceOfficerDetail(ModelDetail, PoliceMixin):
    pass
