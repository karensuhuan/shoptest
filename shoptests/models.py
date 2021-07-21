from django.db import models

#用户表
# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    username = models.CharField(max_length=200)

    class Meta:
        db_table = 'user'
# #商品表
# class Shop(models.Model):
#     shopId = models.CharField(max_length=50)
#
#
#
#
#     class Meta:
#         db_table = 'shop'
# #订单表
# class Order(models.Model):
#
#     class Meta:
#         db_table = 'order'
#
# #购物车表
# class Car(models.Model):
#
#     class Meta:
#         db_table ='car'