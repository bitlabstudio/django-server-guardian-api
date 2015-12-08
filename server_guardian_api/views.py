"""Views for the server_guardian_api app."""
from django.views.generic import View

from django_libs.views_mixins import JSONResponseMixin
from django_libs.loaders import load_member

from .constants import ERROR_RESPONSE
from .default_settings import PROCESSORS


class ServerGuardianAPIView(JSONResponseMixin, View):
    """
    This view gathers and returns API metrics, that can be returned to the
    ``django-server-guardian``.

    """

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        ctx = []
        for label, processor_path in PROCESSORS:
            processor = load_member(processor_path)
            try:
                ctx.append({label: processor()})
            except Exception as ex:
                info = ERROR_RESPONSE['info']
                response = ERROR_RESPONSE
                response.update({'info': info + str(ex)})
                ctx.append({label: response})
        return ctx
