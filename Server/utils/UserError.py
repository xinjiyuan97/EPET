"""
Title: 用户事物错误
Author: xinjiyuan97
Date: 2018-3-14
TODO: 设定与用户登陆、注册有关的错误
"""

class RegisterTimeOut(Exception):
    def __init__(self):
        err = 'The link is no longer effect.'
        Exception.__init__(self, err)

class RegisterAlready(Exception):
    def __init__(self):
        err = 'The link is no longer effect.'
        Exception.__init__(self, err)

class WrongPassword(Exception):
    def __init__(self):
        err = 'Wrong password!'
        Exception.__init__(self, err)