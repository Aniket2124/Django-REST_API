from django.urls import path
from .views import StudentListView,StudentCreateView,StudentUpdateView, StudentDeleteView

urlpatterns = [
   
    path('', StudentListView.as_view(),name="stud_list" ),
    path('create/', StudentCreateView.as_view(),name="create" ),
    path('update/<int:pk>/', StudentUpdateView.as_view(),name="update" ),
    path('delete/<int:pk>/', StudentDeleteView.as_view(),name="delete" ),


]