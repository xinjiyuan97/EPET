"""
Title: 用户邮件认证
Author: xinjiyuan97
Date: 2018-3-14
TODO: 用于进行用户的邮件认证，通过发送给用户的链接进行验证
"""

import datetime
from utils.UserError import RegisterTimeOut, RegisterAlready
from users.models import UserInfo
from django.shortcuts import render

def checkDate(person):
    # TODO: 检查链接是否过期
    if person.tokenExptime.replace(tzinfo = None) < datetime.datetime.now():
        raise RegisterTimeOut()

def changeStatus(person):
    # TODO: 更改用户注册状态，若已经
    if person.status:
        raise RegisterAlready()
    person.status = True
    person.save()

def filledTemplate(request, mess, temp = 'web/varify.html'):
    html = render(request, temp, {'varifyMessage': mess})
    return html

def confirm(request, token):
    try:
        print(token)
        person = UserInfo.objects.get(actiCode = token)
        checkDate(person)
        changeStatus(person)
    except UserInfo.DoesNotExist as e:
        return filledTemplate(request, e)
    except RegisterTimeOut as e:
        return filledTemplate(request, e)
    except RegisterAlready as e:
        return filledTemplate(request, e)
    return filledTemplate(request, "Success!")


# 用户邮件验证