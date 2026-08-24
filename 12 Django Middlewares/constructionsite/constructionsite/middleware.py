from django.conf import settings
from django.http import HttpResponse

# Request Middleware 
class UnderConstructionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path != "/under_construction/" and settings.SITE_UNDER_CONSTRUCTION:
            return HttpResponse("Site Is Under Construction. Please Check Back Later!")

        response = self.get_response(request)
        return response

class FooterAppendMiddleware:
    def __init__(self, get_response):
            self.get_response = get_response
    
    def __call__(self, request):
        response = self.get_response(request)
        if "text/html" in response.get("Content-Type", ""):
              footer_message = "<footer><p>Powered By Djnago</p></footer>"
              content = response.content.decode("utf-8")
              content = content.replace("</body>", f"{footer_message}</body>")
              response.content = content.encode("utf-8")
        return response             

import logging
from django.http import JsonResponse
logger = logging.getLogger(__name__)
class ExceptionLoggingMiddleware:
    def __init__(self, get_response):
                 self.get_response = get_response
         
    def __call__(self, request):
        try:
            if request.path == "/test-exception/":
                raise RuntimeError("Triggered Middleware Exception for Testing!")
            response = self.get_response(request)
            return response
        except Exception as e:
            logger.exception("Unhandled exception caught by middleware")
            return JsonResponse(
                {"error": "Internal Server Error"},
                status=500
            )
