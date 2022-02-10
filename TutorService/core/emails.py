from django.templatetags.static import static

from ..core.utils import build_absolute_uri


def get_email_base_context():
    domain = 'domain'
    name = 'TutorService'
    logo_url = build_absolute_uri(static("images/logo-light.svg"))
    return {"domain": domain, "logo_url": logo_url, "site_name": name}