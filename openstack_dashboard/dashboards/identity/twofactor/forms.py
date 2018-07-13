import random

from django.utils.translation import ugettext_lazy as _

from horizon import exceptions
from horizon import forms
from horizon import messages

from openstack_dashboard.api import jt


class CreateFactorForm(forms.SelfHandlingForm):
    name = forms.CharField(label=_("Factor Name"))

    def handle(self, request, data):
        try:
            secret = self._generate_secret()
            jt.set_totp_secret(request.user.id, data["name"], secret)
            messages.success(request, _("Factor created successfully."))
        except Exception:
            exceptions.handle(request, _('Unable to create factor.'))

    def _generate_secret(self):
        chars = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ234567')
        r = random.SystemRandom()
        return ''.join(r.choice(chars) for _ in range(16))
