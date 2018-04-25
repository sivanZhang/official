# -*- conding:utf-8 -*- 
import pdb
import requests
from django.conf import settings
from book.models import AdaptorBook as Book
from common.e_mail import EmailEx

def pay_book(billno, pay_way, payed_money, trade_no, pay_datetime):
    """
    填写订单支付信息:支付方式、支付金额，支付订单号，支付时间
    验证信息：支付金额需要跟应付金额相同，否则列为异常订单
    """
    result = {}
    book = Book.objects.get(billno = billno)
    if book.status == Book.STATUS_CREATED:
        result['created'] = True 
    result['book'] = book 
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
    #返回成功页面 
    if 'created' in result:
        emailex = EmailEx()
        emailcontent = """
        您好！
        <br/>
        <br/>
        您已成功预约ASU Watch，预约码为xxx，如有货会第一时间给您发短信/邮件通知。您在购买结算时输入预约码可直接抵扣200元现金。请妥善保留此邮件!
        <br/>
        <br/>
        一数科技商城
        """
        smscontent = """您好，您已成功预约ASU Watch，预约码为xxx，如有货会第一时间给您发短信通知。您在购买结算时输入预约码可直接抵扣200元现金。请妥善保留此短信"""
        emailcontent = emailcontent.replace('xxx', book.billno)
        smscontent = smscontent.replace('xxx', book.billno)
    
        emailex.send_text_email("一数科技预约支付", emailcontent, book.email)
        sendsms(book.phone, smscontent)

    return result


def sendsms(phone, content):
    content = content + ' 【一数科技】'
    req = requests.get(settings.SMS_API.format(phone, content) )
    