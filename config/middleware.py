# middleware.py
from django.conf import settings
from django.http import HttpResponseBadRequest

class DisableAllowedHostsForELB:
    """
    Middleware pour bypasser ALLOWED_HOSTS sur les requêtes ELB (HealthCheck).
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user_agent = request.META.get("HTTP_USER_AGENT", "")
        if user_agent.startswith("ELB-HealthChecker"):
            # Override le header Host pour bypass ALLOWED_HOSTS
            # On force un Host "allowed"
            request.META['HTTP_HOST'] = settings.ALLOWED_HOSTS[0] if settings.ALLOWED_HOSTS else "localhost"
            
        response = self.get_response(request)
        return response

