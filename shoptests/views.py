import json

import jwt
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render



from shoptests.models import User


def register(request):
    data = json.loads(request.body)

    User.objects.create(**data)

    return JsonResponse({"code":200})



def login(request):
    data = json.loads(request.body)
    email = data.get('email')
    password = data.get('password')
    user = User.objects.filter(email=email,password=password)
    if not user:
        return JsonResponse({"code":400})

    # response = JsonResponse({"code":200})
    # print(request)
    # response.set_cookie("key","123")
    #
    # request.session['key']="4577"

    payload = {
        "email": email
    }

    token = jwt.encode(payload, "SECRET_KEY", algorithm="HS256").decode('utf-8')
    #token = jwt.encode(payload, "SECRET_KEY", algorithm="HS256").decode('utf-8')

    return JsonResponse({
        "code":200,
        "authToken":token
    })
# class CartAddView(View):
#     def post(self,request):
#         user = request.user
#         if not user.is_authenticated():
#             return JsonResponse({
#               'res':0,
#               'errmsg':'请先登录'
#             })
#         sku_id = request.POST.get('sku_id')
#         count = request.POST.get('count')
#         #数据校验
#         if not all([sku_id,count]):
#             return JsonResponse({
#                 'res':1,
#                 'errmsg':'数据不完整'
#             })
#
#         #校验添加的商品数量
#         try:
#             count = int(count)
#         except Exception as e:
#             return JsonResponse({
#             'res':2,
#             'errmsg':'商品数目出错'
#         })
#     #校验商品是否存在
#         try:
#             sku = GoodsSKU.OBJECTS.get(id = sku_id)
#         except GoodsSKU.objects.DoesNoteExist:
#             return JsonResponse({
#                 'res':3,
#                 'errmsg':"商品不存在"
#         })
#         #业务处理，添加购物车记录
#         conn = get_redis_connection('default')
#         cart_key = 'car_%d' % user.id
#         #先尝试获取sku_id的值
#         #hset->如果sku_id不存在hget返回none
#         car_count = conn.hget(cart_key,sku_id)
#         if car_count:
#             count+=int(car_count)
#
#
#         #校验商品库存
#         if count>sku.stock:
#             return JsonResponse({
#                 'res':4,
#                 'errmsg':'商品库存不足'
#             })
#         conn.set(cart_key,sku_id,car_count)
#         total_count = conn.hlen(cart_key)
#
#         return JsonResponse({
#             'res':5,
#             'total_count':total_count,
#             'message':'添加成功'
#         })


#登录

#注册
#修改密码
#查看商品
#添加购物车
#编辑购物车
#下单
#查看订单
