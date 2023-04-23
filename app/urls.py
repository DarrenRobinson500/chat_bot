from django.urls import path
# from . import views
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('past', past, name="past"),
    path('delete/<id>', delete, name="delete"),
    path('label_answer/<item_id>/<label_id>', label_answer, name='label_answer'),
    path('label_filter/<label_id>', label_filter, name='label_filter'),
    path('new_label', new_label, name='new_label')
]
