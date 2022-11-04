from django.urls import path
from.views import CreateUserView,RetrieveUpdateDestroyUserView

urlpatterns = [
    path('', CreateUserView.as_view(), name= 'craete'),
    path('retrive_update_destroy/<int:pk>/', RetrieveUpdateDestroyUserView.as_view(), name= 'retrive_update_destroy'),
]