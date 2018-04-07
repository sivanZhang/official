# -*- conding:utf-8 -*- 
import pdb
import requests
from django.conf import settings
from book.models import AdaptorBook as Book
 

def pay_book(billno, pay_way, payed_money, trade_no, pay_datetime):
    """
    填写订单支付信息:支付方式、支付金额，支付订单号，支付时间
    验证信息：支付金额需要跟应付金额相同，否则列为异常订单
    """
    result = {}
    book = Book.objects.get(billno = billno)
    
    book.status = book.STATUS_PAYED
    book.money = payed_money
    book.pay_way = pay_way
    book.payed_money = payed_money
    book.trade_no = trade_no
    book.pay_datetime = pay_datetime
    result['status']  = 'ok'
    result['msg'] = "saved" 
    book.save()
    result['book'] = book 

    return result


def sendsms(phone, content):
    req = requests.get(settings.SMS_API.format(phone, content) ) 