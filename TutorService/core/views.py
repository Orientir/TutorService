from django.template.response import TemplateResponse


def home(request):
    return TemplateResponse(request, "home.html",)

def handle_404(request, exception=None):
    return TemplateResponse(request, "404.html", status=404)
