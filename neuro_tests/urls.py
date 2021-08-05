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

from med_tests.views import PassDepressionTest, PassSensitizationTest

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include(('med_tests.urls', 'med_tests'), namespace='med_tests')),
    path('depression_test/', PassDepressionTest.as_view(), name="pass_depression_test"),
    path('sensitization_test/', PassSensitizationTest.as_view(), name="pass_sensitization_test")
]
