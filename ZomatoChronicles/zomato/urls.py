from django.urls import path
from . import views

urlpatterns = [
    path('', views.menushow, name='menu'),
    path('add', views.addDish, name='add'),
    path('delete/<int:id>', views.DeleteDish, name='delete'),
    path('update/<int:id>', views.UpdateDish, name='update'),
    path('takeorder', views.TakeOrder, name='takeorder'),
    path('order', views.reviewOrder, name='order'),
    path('update_status/<int:orderID>', views.UpdateStatus, name='update_status'),
]