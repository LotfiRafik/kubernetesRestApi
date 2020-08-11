from django.shortcuts import render
import requests

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.db.models import F, Max, Sum
from django.http import Http404, HttpResponseForbidden

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView

# Create your views here.


class ClusterList(APIView):
    """
    List all Clusters,Create new Cluster
    """
    def get(self, request, format=None):
        pass

class ClusterDetail(APIView):
    """
    Cluster Detail (information)
    """
    def get(self, request, id, format=None):
        pass

class NodeList(APIView):
    """
    List nodes per cluster , Create new Node
    """

    def get(self, request, id, format=None):
        # First we should get the IP addresse of the cluster identified by its ID from the database 
        # and the token to access its api-server
        # Make a get request to get the list of nodes from the kubernetes api-server .

        token = "eyJhbGciOiJSUzI1NiIsImtpZCI6Im16UEdMV3kxVGoyMkc1cFFBUmxHOHJUMFdfS0oxYzZGczVDbkg5SjFKRU0ifQ.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJrdWJlLXN5c3RlbSIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VjcmV0Lm5hbWUiOiJkZWZhdWx0LXRva2VuLXRicnRyIiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZXJ2aWNlLWFjY291bnQubmFtZSI6ImRlZmF1bHQiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC51aWQiOiIyOWI3MDZjNy0zODljLTRiN2UtYjc0ZS1mYjY1YjYyYmM2MTQiLCJzdWIiOiJzeXN0ZW06c2VydmljZWFjY291bnQ6a3ViZS1zeXN0ZW06ZGVmYXVsdCJ9.3waXSLhBQeC6NXBeib6_QH4Rdk0XUBHCvshhGQ-pzvE_x2PuwxXXYT8XCjoA7sa4QBB-c57gZTJy79GFNYver2YYZh-NMR9vrPrKgkHJQ9Bnm5Wvc3-kZ5UPEJJeo3-m0OicehBgcOvhiEwcNNMC8_JLHMiJ9daa-zwKXE7hElGHG6B2j_2Wt6hbH-sf-5iJUliqcQkwSTv-Wvs3Nc9wK3qkvqKTJBfJSYQCzYYXmIiO6JOHOzsEYzXVLG2516ncv4_qMtUqy-pqg_ReM9bYY3pU7e2xdljYxFVCyeyoHy7TFrsggKoPdWaf01dquTMXpHaQT4oIFv3a1IOWUjkvuA"
        response = requests.get("https://192.168.99.100:8443/api/v1/nodes/", headers={'Authorization': 'Bearer ' + token}, verify=False)
        print(type(response.json()))
        return Response(response.json()) 

class NodeDetail(APIView):
    """
    Node Detail (information)
    """
    def get(self, request, id, format=None):
        pass

class PodList(APIView):
    """
    List pods per cluster , Deploy new pod
    """
    def get(self, request, clusterid, format=None):
        # First we should get the IP addresse of the cluster identified by its ID from the database 
        # and the token to access its api-server
        # Make a get request to get the list of nodes from the kubernetes api-server .
        token = "eyJhbGciOiJSUzI1NiIsImtpZCI6Im16UEdMV3kxVGoyMkc1cFFBUmxHOHJUMFdfS0oxYzZGczVDbkg5SjFKRU0ifQ.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJrdWJlLXN5c3RlbSIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VjcmV0Lm5hbWUiOiJkZWZhdWx0LXRva2VuLXRicnRyIiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZXJ2aWNlLWFjY291bnQubmFtZSI6ImRlZmF1bHQiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC51aWQiOiIyOWI3MDZjNy0zODljLTRiN2UtYjc0ZS1mYjY1YjYyYmM2MTQiLCJzdWIiOiJzeXN0ZW06c2VydmljZWFjY291bnQ6a3ViZS1zeXN0ZW06ZGVmYXVsdCJ9.3waXSLhBQeC6NXBeib6_QH4Rdk0XUBHCvshhGQ-pzvE_x2PuwxXXYT8XCjoA7sa4QBB-c57gZTJy79GFNYver2YYZh-NMR9vrPrKgkHJQ9Bnm5Wvc3-kZ5UPEJJeo3-m0OicehBgcOvhiEwcNNMC8_JLHMiJ9daa-zwKXE7hElGHG6B2j_2Wt6hbH-sf-5iJUliqcQkwSTv-Wvs3Nc9wK3qkvqKTJBfJSYQCzYYXmIiO6JOHOzsEYzXVLG2516ncv4_qMtUqy-pqg_ReM9bYY3pU7e2xdljYxFVCyeyoHy7TFrsggKoPdWaf01dquTMXpHaQT4oIFv3a1IOWUjkvuA"
        api_endpoint = "https://192.168.99.100:8443/api/v1/"

        #get pods only in a given namespaces
        if 'namespace' in request.GET:
            namespace = request.GET['namespace']
            api_endpoint += "namespaces/"+namespace+"/"

        api_endpoint += "pods/"
        response = requests.get(api_endpoint, headers={'Authorization': 'Bearer ' + token}, verify=False)
        return Response(response.json())
    
    def post(self, request, clusterid, format=None):
        token = "eyJhbGciOiJSUzI1NiIsImtpZCI6Im16UEdMV3kxVGoyMkc1cFFBUmxHOHJUMFdfS0oxYzZGczVDbkg5SjFKRU0ifQ.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJrdWJlLXN5c3RlbSIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VjcmV0Lm5hbWUiOiJkZWZhdWx0LXRva2VuLXRicnRyIiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZXJ2aWNlLWFjY291bnQubmFtZSI6ImRlZmF1bHQiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC51aWQiOiIyOWI3MDZjNy0zODljLTRiN2UtYjc0ZS1mYjY1YjYyYmM2MTQiLCJzdWIiOiJzeXN0ZW06c2VydmljZWFjY291bnQ6a3ViZS1zeXN0ZW06ZGVmYXVsdCJ9.3waXSLhBQeC6NXBeib6_QH4Rdk0XUBHCvshhGQ-pzvE_x2PuwxXXYT8XCjoA7sa4QBB-c57gZTJy79GFNYver2YYZh-NMR9vrPrKgkHJQ9Bnm5Wvc3-kZ5UPEJJeo3-m0OicehBgcOvhiEwcNNMC8_JLHMiJ9daa-zwKXE7hElGHG6B2j_2Wt6hbH-sf-5iJUliqcQkwSTv-Wvs3Nc9wK3qkvqKTJBfJSYQCzYYXmIiO6JOHOzsEYzXVLG2516ncv4_qMtUqy-pqg_ReM9bYY3pU7e2xdljYxFVCyeyoHy7TFrsggKoPdWaf01dquTMXpHaQT4oIFv3a1IOWUjkvuA"
        api_endpoint = "https://192.168.99.100:8443/api/v1/"

        #Must specify the namespace where to create the POD
        if 'namespace' not in request.GET:
            response = {'error':'namespace in get parameteres is required'}
            return Response(response.json())

        namespace = request.GET['namespace']
        api_endpoint += "namespaces/"+namespace+"/"
        api_endpoint += "pods/"
        #the body of the POST request must be json data
        data = request.body
        response = requests.post(api_endpoint, data=data, headers={'Authorization': 'Bearer ' + token}, verify=False)
        return Response(response.json(), status=response.status_code)

class PodDetail(APIView):
    """
    Pod Detail (information) in a given cluster , namespace
    """
    def get(self, request, clusterid, podid, format=None):
        token = "eyJhbGciOiJSUzI1NiIsImtpZCI6Im16UEdMV3kxVGoyMkc1cFFBUmxHOHJUMFdfS0oxYzZGczVDbkg5SjFKRU0ifQ.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJrdWJlLXN5c3RlbSIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VjcmV0Lm5hbWUiOiJkZWZhdWx0LXRva2VuLXRicnRyIiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZXJ2aWNlLWFjY291bnQubmFtZSI6ImRlZmF1bHQiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC51aWQiOiIyOWI3MDZjNy0zODljLTRiN2UtYjc0ZS1mYjY1YjYyYmM2MTQiLCJzdWIiOiJzeXN0ZW06c2VydmljZWFjY291bnQ6a3ViZS1zeXN0ZW06ZGVmYXVsdCJ9.3waXSLhBQeC6NXBeib6_QH4Rdk0XUBHCvshhGQ-pzvE_x2PuwxXXYT8XCjoA7sa4QBB-c57gZTJy79GFNYver2YYZh-NMR9vrPrKgkHJQ9Bnm5Wvc3-kZ5UPEJJeo3-m0OicehBgcOvhiEwcNNMC8_JLHMiJ9daa-zwKXE7hElGHG6B2j_2Wt6hbH-sf-5iJUliqcQkwSTv-Wvs3Nc9wK3qkvqKTJBfJSYQCzYYXmIiO6JOHOzsEYzXVLG2516ncv4_qMtUqy-pqg_ReM9bYY3pU7e2xdljYxFVCyeyoHy7TFrsggKoPdWaf01dquTMXpHaQT4oIFv3a1IOWUjkvuA"
        api_endpoint = "https://192.168.99.100:8443/api/v1/"

        #Must specify the namespace where to find the POD
        if 'namespace' not in request.GET:
            response = {'error':'namespace in get parameteres is required'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        namespace = request.GET['namespace']
        api_endpoint += "namespaces/"+namespace+"/"

        api_endpoint += "pods/"+podid+"/"

        response = requests.get(api_endpoint, headers={'Authorization': 'Bearer ' + token}, verify=False)
        return Response(response.json(), status=response.status_code)

    def delete(self, request, clusterid, podid, format=None):
        token = "eyJhbGciOiJSUzI1NiIsImtpZCI6Im16UEdMV3kxVGoyMkc1cFFBUmxHOHJUMFdfS0oxYzZGczVDbkg5SjFKRU0ifQ.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJrdWJlLXN5c3RlbSIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VjcmV0Lm5hbWUiOiJkZWZhdWx0LXRva2VuLXRicnRyIiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZXJ2aWNlLWFjY291bnQubmFtZSI6ImRlZmF1bHQiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC51aWQiOiIyOWI3MDZjNy0zODljLTRiN2UtYjc0ZS1mYjY1YjYyYmM2MTQiLCJzdWIiOiJzeXN0ZW06c2VydmljZWFjY291bnQ6a3ViZS1zeXN0ZW06ZGVmYXVsdCJ9.3waXSLhBQeC6NXBeib6_QH4Rdk0XUBHCvshhGQ-pzvE_x2PuwxXXYT8XCjoA7sa4QBB-c57gZTJy79GFNYver2YYZh-NMR9vrPrKgkHJQ9Bnm5Wvc3-kZ5UPEJJeo3-m0OicehBgcOvhiEwcNNMC8_JLHMiJ9daa-zwKXE7hElGHG6B2j_2Wt6hbH-sf-5iJUliqcQkwSTv-Wvs3Nc9wK3qkvqKTJBfJSYQCzYYXmIiO6JOHOzsEYzXVLG2516ncv4_qMtUqy-pqg_ReM9bYY3pU7e2xdljYxFVCyeyoHy7TFrsggKoPdWaf01dquTMXpHaQT4oIFv3a1IOWUjkvuA"
        api_endpoint = "https://192.168.99.100:8443/api/v1/"

        #Must specify the namespace where to find the POD
        if 'namespace' not in request.GET:
            response = {'error':'namespace in get parameteres is required'}
            return Response(response.json())

        namespace = request.GET['namespace']
        api_endpoint += "namespaces/"+namespace+"/"

        api_endpoint += "pods/"+podid+"/"

        response = requests.delete(api_endpoint, headers={'Authorization': 'Bearer ' + token}, verify=False)
        return Response(response.json(), status=response.status_code)



class NodePodList(APIView):
    """
    List all pods,Deploy new pod
    """
    def get(self, request, format=None):
        pass