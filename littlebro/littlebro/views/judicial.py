from django.views.generic import ListView
from littlebro.models import Judge

class Judge(ListView):
    model = Judge
    template_name = "object_list.html"
