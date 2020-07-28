from django.shortcuts import render
from django.contrib.auth.models import User
from test_app.models import *
from django.contrib.auth import authenticate,login,logout
from rest_framework.decorators import api_view,permission_classes
from rest_framework.status import HTTP_400_BAD_REQUEST,HTTP_404_NOT_FOUND,HTTP_200_OK
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from test_app.serializers import UserSerializer

#endpoint for user signup
@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny,))
def user_login(request): #login a user
    username = request.data.get('username')
    passw=request.data.get('password')
    u=authenticate(username=username,password=passw)
    if not u:
        return Response({'status':'failure','data':{'message':'wrong username or password'}},status=HTTP_400_BAD_REQUEST)
    # token,x=Token.objects.get_or_create(user=u)
    return Response({'status':'success','data':{'message':u.id}}, status=HTTP_200_OK)

#endpoint for user signup
@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny,))
def user_register(request):
	username = request.data.get('username')
	first_name=request.data.get('first_name')
	last_name = request.data.get('last_name')
	passw = request.data.get('password')
	if User.objects.filter(username=username). exists():
		return Response({'status':'failure','data':{'message':'Username already exists'}},status=HTTP_400_BAD_REQUEST)
	user_obj=User.objects.create_user(username=username,password=passw,first_name=first_name,last_name=last_name)
	user_obj.save()
	UserDetails.objects.create(user_acc=user_obj)
	return Response({'status':'success','data':{'message':'Account Created'}},status=HTTP_200_OK)

#user logout
@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny,))
def user_logout(request):
    request.user.auth_token.delete() 
    logout(request)
    Response({'status':'success','data':{'message':'Logged out'}},status=HTTP_200_OK)


# Fetch User notes
@api_view(['GET'])
def notes_list(request,pk):
	try :
		user = UserDetails.objects.get(pk=pk)
	except UserDetails.DoesNotExist:
		return Response({'status':'failure','data':{'message':'User does not exists'}},status=HTTP_400_BAD_REQUEST)

	if request.method == 'GET' :
		user_serializer = UserSerializer(user)
		return Response({'status': 'success', 'data': {user.note}}, status=HTTP_200_OK)
		
@api_view(['POST'])
def get_user_info(request,pk):
	
	try :
		user = UserDetails.objects.get(pk=pk)
	except UserDetails.DoesNotExist:
		return Response({'status':'failure','data':{'message':'User does not exists'}},status=HTTP_400_BAD_REQUEST)

	if request.method=='POST' :
		notes = request.data.get('notes')
		user.note.append(notes)
		user.save()
	return Response({'status': 'success', 'data': {'message': 'Notes Added', 'notes' : user.note}}, status=HTTP_200_OK)