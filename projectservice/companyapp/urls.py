from django.urls import path
from .views import *

urlpatterns = [
   path('company/',Companyview.as_view()),
  
]