"""kuberestapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from .views import *

urlpatterns = [

    #List clusters "HTTP GET", Add new Cluster "HTTP POST"
    path('', ClusterList.as_view()),

    #Cluster Detail (information) "HTTP GET"
    path('<int:id>/', ClusterDetail.as_view()),
    
    #List nodes cluster "HTTP GET", Add node to the cluster "HTTP POST"
    path('<int:id>/node/', NodeList.as_view()),
    
    #List pods per cluster "HTTP GET", Deploy pod to the cluster "HTTP POST"
    path('<int:clusterid>/pod/', PodList.as_view()),

    #Pod Detail (information) "HTTP GET" , Modify pod "HTTP PATCH/PUT" , Delete pod "HTTP DELETE"
    path('<int:clusterid>/pod/<str:podid>/', PodDetail.as_view()),

    #Node Detail (information) "HTTP GET" , Modify node "HTTP PATCH/PUT" , Delete node "HTTP DELETE"
    #Node can be 'master node' or 'worker node' 
    path('<int:id>/node/<int:nodeid>/', NodeDetail.as_view()),

    #List pods per node "HTTP GET"
    path('<int:id>/node/<int:nodeid>/pod/', NodePodList.as_view()),

]
