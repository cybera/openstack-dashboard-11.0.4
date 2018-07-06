import base64
import random
import string

from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as _

from horizon import forms
from horizon import tables

from openstack_dashboard.dashboards.identity.twofactor \
    import forms as twofactor_forms
from openstack_dashboard.dashboards.identity.twofactor \
    import tables as twofactor_tables

class IndexView(tables.DataTableView):
    table_class = twofactor_tables.FactorsTable
    #template_name = 'identity/users/index.html'
    page_title = "Two-factor Authentication"

    def has_more_data(self, table):
	return False
        #return self._more

    def get_data(self):
        data = [
            Factor(1, "Foo"),
            Factor(2, "Bar"),
            Factor(3, "Baz")
        ]
        return data

class CreateView(forms.ModalFormView):
    template_name = 'identity/users/create.html'
    modal_header = _("Create Factor")
    form_id = "create_factor_form"
    form_class = twofactor_forms.CreateFactorForm
    submit_label = _("Create Factor")
    submit_url = reverse_lazy("horizon:identity:2fa:create")
    success_url = reverse_lazy('horizon:identity:2fa:index')
    page_title = _("Create Factor")

class Factor(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.secret = self._rand_str()

    def _rand_str(self):
        return ''.join([random.choice(string.lowercase) for i in xrange(26)])
