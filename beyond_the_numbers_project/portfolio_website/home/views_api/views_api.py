from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from rest_framework import permissions
from ..models import Matches
from .. import serializers
from django.shortcuts import render

def my_view(request):
    mymatches = Matches.objects.all()
    context = {'mymodels': mymatches}
    return render(request, 'api.html', context)

class MatchesListApiView(APIView):
    def get(self,request,*args,**kwargs):
        mymatches = Matches.objects.all().using('sports_analysis')
        serializer = serializers.MatchesSerializer(mymatches,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    

    
