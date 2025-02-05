from django.contrib import admin
from django.urls import path,include
from Visualization import views
urlpatterns = [
    path("adminpage",views.home,name="home"),
    path("",views.homepage,name="homepage"),
    path("total",views.total_impact),
    path("org",views.organization),
    path("detail/<int:id>",views.detail),
    path("chatbot",views.chatbot),
    path('get_qa_model', views.get_qa_model, name='get_qa_model'),
    path("upload",views.upload),
    path("add/<int:id>",views.add),
]