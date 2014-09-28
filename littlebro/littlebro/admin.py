from django.contrib.admin.sites import AdminSite
from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatPageAdmin as FlatPageAdminOld
from django.contrib.flatpages.admin import FlatpageForm as FlatpageFormOld

from grappelli.forms import GrappelliSortableHiddenMixin

from django import forms
from ckeditor.widgets import CKEditorWidget

from littlebro.models import Tag, Rating
from littlebro.models import Police, District, Rank


class FlatpageForm(FlatpageFormOld):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = FlatPage # this is not automatically inherited from FlatpageFormOld


class FlatPageAdmin(FlatPageAdminOld):
    form = FlatpageForm


#
# Executive
#

class RankInline(GrappelliSortableHiddenMixin, admin.TabularInline):
    model = Rank

    sortable_field_name = 'rank'


class DistrictModelAdmin(admin.ModelAdmin):

    inlines = [
        RankInline
    ]

# We have to unregister the normal admin, and then reregister ours
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)

admin.site.register(District, DistrictModelAdmin)
admin.site.register(Police)
admin.site.register(Rank)
admin.site.register(Tag)
admin.site.register(Rating)
