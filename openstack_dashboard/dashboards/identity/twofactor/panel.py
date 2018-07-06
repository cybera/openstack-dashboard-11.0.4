from django.utils.translation import ugettext_lazy as _

import horizon

class TwoFactorAuth(horizon.Panel):
    name = _("Two-factor")
    slug = '2fa'

    def can_access(self, context):
        return True
