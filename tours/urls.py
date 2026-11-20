from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("packages/", views.package_list, name="packages"),
    path("packages/<int:pk>/", views.package_detail, name="package_detail"),
    path("booking/", views.booking_create, name="booking"),
    path("contact/", views.contact, name="contact"),
    path("gallery/", views.gallery, name="gallery"),
    path("reviews/", views.reviews, name="reviews"),
    path("about/", views.about, name="about"),
    path("feedback/", views.feedback, name="feedback"),
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="home"), name="logout"),
    path("signup/", views.signup, name="signup"),  
]
