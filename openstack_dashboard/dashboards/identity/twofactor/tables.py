from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ungettext_lazy

from horizon import forms
from horizon import tables

from openstack_dashboard.api import jt

class CreateFactor(tables.LinkAction):
    name = "create"
    verbose_name = _("Create Factor")
    url = "horizon:identity:2fa:create"
    classes = ("ajax-modal",)
    icon = "plus"

class DeleteFactorsAction(tables.DeleteAction):
    @staticmethod
    def action_present(count):
        return ungettext_lazy(
            u"Delete Factor",
            u"Delete Factors",
            count
        )

    @staticmethod
    def action_past(count):
        return ungettext_lazy(
            u"Deleted Factor",
            u"Deleted Factors",
            count
        )

    def delete(self, request, obj_id):
        jt.delete_totp_secret(obj_id)

class UpdateRow(tables.Row):
    ajax = True

    def get_data(self, request, obj_id):
        pass

class FactorsTable(tables.DataTable):
    id = tables.Column('id', verbose_name=_('ID'),
            form_field=forms.IntegerField())
    name = tables.Column('name', verbose_name=_('Name'),
                           form_field=forms.CharField(max_length=64))
    secret = tables.Column('secret', verbose_name=_('Secret'),
                           form_field=forms.CharField(max_length=64))

    class Meta(object):
        name = "factors"
        verbose_name = _("Factors")
        row_class = UpdateRow
        row_actions = (DeleteFactorsAction,)
        table_actions = (CreateFactor, DeleteFactorsAction)
        pagination_param = "factor_marker"

