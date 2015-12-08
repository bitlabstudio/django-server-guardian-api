"""Tests for the views of the ``server_guardian_api`` app."""
from django.test import TestCase

from django_libs.tests.mixins import ViewRequestFactoryTestMixin

from .. import views


class ServerGuardianAPIViewTestCase(ViewRequestFactoryTestMixin, TestCase):
    """Tests for the ``ServerGuardianAPIView`` view class."""
    view_class = views.ServerGuardianAPIView

    def test_view(self):
        self.is_callable()
