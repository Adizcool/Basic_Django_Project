from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
import pandas as pd

# Create your views here.

#All logic and APIs created here

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def get_sites(request):
    if request.method == 'GET':
        site_obj = Site.objects.all()
        serializer = SiteSerializer(site_obj, many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # import pdb;pdb.set_trace()
        sites = request.data
        serializer = SiteSerializer(data=sites)
        if serializer.is_valid():
            serializer.save()
            return Response('Data saved successfully')

    elif request.method == 'PUT':
        primary = request.query_params.get('site_id', None)
        if primary:
            site = Site.objects.get(pk = primary)
            serializer = SiteSerializer(data=request.data, instance = site)
            if serializer.is_valid():
                serializer.save()
                return Response('sites Updated')
            return Response("bad request")
        return Response("Not found")

    elif request.method == 'PATCH':
        primary = request.query_params.get('site_id', None)
        if primary:
            site = Site.objects.get(pk = primary)
            serializer = SiteSerializer(data=request.data, instance = site, partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response('sites Updated')
            return Response("bad request")
        return Response("Not found")

    elif request.method == 'DELETE':
        pk = request.query_params.get('site_id', None)
        site = Site.objects.get(pk=pk).delete()
        return Response('sites Deleted')


#Using Class based API here. Similar as before, just using function instead of decorators and if statements
#For checking HTTP method

class Site_list(APIView):
    def get(self, request, format = None):
        site_obj = Site.objects.all()
        serializer = SiteSerializer(site_obj, many=True)
        return Response(serializer.data)

    def post(self, request, format = None):
        serializer = SiteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Data added successfully")
        return Response("Bad Request")

    def put(self, request, format = None):
        primary = request.query_params.get('site_id', None)
        if primary:
            site = Site.objects.get(pk = primary)
            serializer = SiteSerializer(data = request.data, instance = site)
            if serializer.is_valid():
                serializer.save()
                return Response("Data Changed")
            return Response("Bad Request")
        return Response("Data not found")

    def patch(self, request, format = None):
        primary = request.query_params.get('site_id', None)
        if primary:
            site = Site.objects.get(pk = primary)
            serializer = SiteSerializer(data = request.data, instance = site, partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response("Data updated")
            return Response("Bad Request")
        return Response("No such data found")

    def delete(self, request, format = None):
        primary = request.query_params.get('site_id', None)
        site = Site.objects.get(pk = primary).delete()
        return Response('Site deleted')

class get_excel(APIView):
    def post(self, request, format = None):
        file = request.FILES['iap_requirements']
        data = pd.read_excel(file)
        for i in data:
            pass
        pass