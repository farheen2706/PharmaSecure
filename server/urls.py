"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
from files.views import addDataRecord# ✅ Ensure this import is correct
from files.views import CompanyData
from files import views  # ✅ Correct if views.py is in files/



app_name = 'files'

urlpatterns = [
    path('managerRegister/', views.managerRegister, name='manReg'),
    path('managerLogin/', views.managerLogin, name='manLog'),
    path('employeeLogin/', views.employeeLogin, name='empLog'),
    path('newPassword/', views.newPassword, name='newPass'),
    path('addEmployee/', views.addEmployee, name='addEmployee'),
    path('logs/', views.logs, name='logs'),
    path('display/', views.display, name='display'),
    path('companyData/', views.CompanyData, name='logout'),
    path("employee/<int:employee_id>/", views.addDataRecord, name="addDataRecord"),
    path("managerDashboard/", views.managerDashboard, name="managerDashboard"),
    path("admin/", admin.site.urls),
    path("", include("files.urls")),

    # path('<int:med_id>/',views.add_component,name='constituent'),
    # path('list/',views.home,name='home'),
    # path('list/<int:id>/',views.retrieve_components,name='retrieve'),
]

