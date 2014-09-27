from django.views.generic import ListView
from littlebro.models import Legislator

class LegislatorList(ListView):
    model = Legislator
    template_name = "object_list.html"
