import pytest
from django.test import RequestFactory
from django.urls import reverse
from geolocation import views

# class TestIndexView:
#   """
#   It's optional to create a class, but it helps to group tests into suites
#   """
#     def test_index(self):
#         req = RequestFactory().get(reverse("geolocation:index"))
#         resp = views.MyView.as_view()(req)
#         assert resp.status_code == 200


class TestIssView:

    def test_iss_people(self):
        req = RequestFactory().get(reverse("geolocation:iss_people"))
        resp = views.iss_people.as_view()(req)
        assert resp.status_code == 200

    def test_iss_location(self):
        req = RequestFactory().get(reverse("geolocation:iss_location"))
        resp = views.iss_location.as_view()(req)
        assert resp.status_code == 200

    def test_iss_info(self):
        req = RequestFactory().get(reverse("geolocation:iss_info"))
        resp = views.iss_info.as_view()(req)
        assert resp.status_code == 200
