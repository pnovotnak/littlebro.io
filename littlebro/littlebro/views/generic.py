from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.views.generic import DetailView


class ModelCreate(CreateView):

    template_name = "littlebro/object_create.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ModelCreate, self).get_context_data(**kwargs)
        context['object_name'] = self.model._meta.verbose_name.title()

        return context


class ModelList(ListView):

    template_name = "littlebro/object_list.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ModelList, self).get_context_data(**kwargs)
        context['object_name'] = self.model._meta.verbose_name.title()
        context['object_name_plural'] = self.model._meta.verbose_name_plural.title()
        context['object_url'] = '%s/%s' % (
            self.model._meta.verbose_name.title().replace(' ', '-').lower(),
            'add',
        )

        return context


class ModelDetail(DetailView):

    template_name = "littlebro/object_detail.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ModelDetail, self).get_context_data(**kwargs)
        context['object_name'] = self.model._meta.verbose_name.title()

        return context
