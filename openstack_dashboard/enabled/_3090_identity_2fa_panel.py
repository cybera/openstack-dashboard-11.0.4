# The slug of the panel to be added to HORIZON_CONFIG. Required.
PANEL = 'Two-Factor Authentication'
# The slug of the dashboard the PANEL associated with. Required.
PANEL_DASHBOARD = 'identity'
# The slug of the panel group the PANEL is associated with.
PANEL_GROUP = 'default'

# Python panel class of the PANEL to be added.
ADD_PANEL = 'openstack_dashboard.dashboards.identity.twofactor.panel.TwoFactorAuth'