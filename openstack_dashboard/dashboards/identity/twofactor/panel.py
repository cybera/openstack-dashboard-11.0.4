from django.utils.translation import ugettext_lazy as _

import horizon

class TwoFactorAuth(horizon.Panel):
    name = _("Two-factor")
    slug = '2fa'

    def can_access(self, context):
        request = context['request']
        for role in request.user.roles:
            if role['name'] == 'admin':
                return True
        return False
