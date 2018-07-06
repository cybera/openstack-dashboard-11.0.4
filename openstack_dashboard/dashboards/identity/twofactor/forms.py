from django.utils.translation import ugettext_lazy as _

from horizon import exceptions
from horizon import forms
from horizon import messages

from openstack_dashboard import api


class CreateFactorForm(forms.SelfHandlingForm):
    name = forms.CharField(label=_("Factor Name"))

    def handle(self, request, data):
        try:
            #new_user = api.keystone.role_create(request, data["name"])
            messages.success(request, _("Factor created successfully."))
            return None
        except Exception:
            exceptions.handle(request, _('Unable to create factor.'))
