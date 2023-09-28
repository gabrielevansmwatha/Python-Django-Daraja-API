from django.urls import path
from . import views

urlpatterns = [
    path('access/',views.get_access_token,name = 'get_access_token'),
    path('push/',views.initiate_stk_push,name = 'initiate_stk_push'),
    path('query/', views.query_stk_status, name='query_stk_status'),
]
