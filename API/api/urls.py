from django.urls import path
from .views import LeadListView, LeadCreateView

urlpatterns = [
   
    path('', LeadListView.as_view(),name="lead_list" ),
    path('create/', LeadCreateView.as_view(),name="create" ),

]