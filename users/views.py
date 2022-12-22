from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from users.models import ZaigoUsers

# Create your views here.

@api_view(['GET'])
def list_user(request):
    data = ZaigoUsers.objects.values('id','name','address','status')
    return Response(data)

@api_view(['POST'])
def fetch_user(request):
    zaigo_user = ZaigoUsers()
    zaigo_user.name = request.data.get('name')
    zaigo_user.dateofbirth = request.data.get('dateofbirth')
    zaigo_user.address = request.data.get('address')
    zaigo_user.save()
    respon = {"msg":"success","data":zaigo_user.id}
    return Response(respon)