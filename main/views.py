from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .serializer import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token

@api_view(['POST'])
def get_token(request):
    try:
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            data = {
                'success': True,
                'user': {
                    "id": user.id,
                    "username": user.username,
                    'token': token.key,
                }
            }
        else:
            data = {
                "success": False,
                "error": "Username or password error!"
            }

    except Exception as err:
        data = {
            "success": False,
            "error": f'{err}'
        }
    return Response(data)


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_user(request):
    user = request.user
    if user.status == 1:
        user = User.objects.all()
        ser = UserSerializer(user, many=True)
        return Response(ser.data)
    else:
        return Response("You can not watch users because you are not director")
        



@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_product(request):
    user = request.user
    if user.status == 1:
        user = Product.objects.all()
        ser = ProductSerializer(user, many=True)
        return Response(ser.data)
    else:
        return Response("You can not watch users because you are not director")
        


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_clients(request):
    user = request.user
    if user.status == 1:
        user = Client.objects.all()
        ser = ClientSerializer(user, many=True)
        return Response(ser.data)
    else:
        return Response("You can not watch users because you are not director")
        



@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_order(request):
    user = request.user
    if user.status == 1:
        user = Order.objects.all()
        ser = OrderSerializer(user, many=True)
        return Response(ser.data)
    else:
        return Response("You can not watch users because you are not director")
        

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_client(request):
    user = request.user
    name = request.POST.get('name')
    debt = request.POST.get('debt')
    if user.status == 2:
        Client.objects.create(name=name, debt=debt)
        return Response("Create client passed very well")
    else:
        return Response("Your status isn`t manager and you cann`t create client")




@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_user(request):
    user = request.user
    username = request.POST.get('username')
    password = request.POST.get('password')
    if user.status == 2:
        User.objects.create(username=username, password=password)
        return Response("Create user passed very well")
    else:
        return Response("Your status isn`t manager and you cann`t create user")


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_order(request):
    user = request.user
    product = request.POST.get('product')
    client = request.POST.get('client')
    date = request.POST.get('date')
    quantity = request.POST.get('quantity')
    if user.statuc == 3:
        Order.objects.create(product_id=product, client_id=client, date=date, quantity=quantity)
        return Response("Create order passed very well")
    else:
        return Response("Your status isn`t call center and you cann`t create order")
    

@api_view(["GET"])
def get_kassa(request):
    pass