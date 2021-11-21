"""neuro_tests URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from med_tests.views import ShowTest, PassTest, ProfilePage, TestList, PatientList, HomePageView, \
    CreateQuestionnairePrescription

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    # path('', include(('med_tests.urls', 'med_tests'), namespace='med_tests')),
    path('test/<int:test_id>/', ShowTest.as_view(), name="show_test"),
    path('test/<int:test_id>/pass/', PassTest.as_view(), name="pass_test"),
    path('profile/<int:user_id>/', ProfilePage.as_view(), name="profile"),
    path('profile/', ProfilePage.as_view(), name="my_profile"),
    path('tests/', TestList.as_view(), name="tests"),
    path('patients/', PatientList.as_view(), name="patients"),
    path('', HomePageView.as_view(), name='home'),
    path('prescribe_test/', CreateQuestionnairePrescription.as_view(), name='prescribe_test')

]
