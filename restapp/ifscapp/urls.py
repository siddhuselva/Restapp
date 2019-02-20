from django.urls import path
from . import views


urlpatterns = [

    path('loadcsv',views.dataload,name = "query"),
    path('dquery',views.dataquery,name = "query"),
    path('dquery/<slug:data>',views.dataquery,name = "query"),
    path('json/', views.d_json, name="suria"),
    path('json/<slug:data>', views.d_jsonb, name="suria"),
    path('json/<slug:data>/<slug:data1>',views.d_jsons ,name='abc'),
    path('json/<slug:data>/<slug:data1>/<slug:data2>',views.d_jsonbr ,name='abc'),
    path('json/<slug:data>/<slug:data1>/<slug:data2>/<slug:data3>',views.d_jsoni ,name='abc'),

]