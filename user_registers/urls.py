from django.urls import path, re_path
from . import views
from .views import (
    home_view,
    register_form,
    login_form,
    registration_bidder_view,
    registration_vendor_view,
    registration_view,
    registered_form,
    login_request,
)


appname = "user_registers"

urlpatterns = [
    path("home/", home_view, name="home_view"),
    path("register_as_user/", register_form, name="register_view"),
    path("login_as_user/", login_form, name="login_view"),
    path(
        "register_as_user/registered_success/", registered_form, name="registered_view"
    ),
    path(
        "registration_success_B/",
        registration_bidder_view,
        name="success_registration_B",
    ),
    path(
        "registration_success_V/",
        registration_vendor_view,
        name="success_registration_V",
    ),
    path(
        "registration_success/<slug:registrar_type>/",
        registration_view,
        name="success_registration",
    ),
    path("login_as_user/login/", login_request, name="loggedin_view"),
]
