import pytest
from django.test import RequestFactory
from django.urls import reverse
from geolocation import views

class TestIndexView:
    """
    It's optional to create a class, but it helps to group tests into suites
    """
    def test_index(self):
        req = RequestFactory().get(reverse("index"))
        resp = views.index(req)
        assert resp.status_code == 200


class TestIssView:

    def test_iss_people(self):
        req = RequestFactory().get(reverse("iss_people"))
        resp = views.iss_people(req)
        assert resp.status_code == 200 

    def test_iss_location(self):
        req = RequestFactory().get(reverse("iss_location"))
        resp = views.iss_location(req)
        assert resp.status_code == 200

    def test_iss_info(self):
        req = RequestFactory().get(reverse("iss_info"))
        resp = views.iss_info(req)
        assert resp.status_code == 200
