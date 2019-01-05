import sys
import os
import time
import datetime
from urllib.request import urlopen

# #实例一:以下仅仅在函数内部定义了一个函数,但并非闭包函数.
# def outer():
#     def inner():
#         print("inner func excuted")
#     inner() #调用执行inner函数
#     print("outer func excuted")
#
# outer()
#
# #实例二:以下在函数内部定义了一个函数，而且还引用了一个外部变量x,那么这个是闭包函数么?答案：不是
# x = 1
# def outer():
#     def inner():
#         print("x=%s" %x)
#         print("inner func excuted")
#     inner()
#     print("outer func excuted")
# outer()


# def outer():
#     x = 1
#     def inner():
#         print("x=%s" %x)
#         print("inner func excuted")
#     # inner()
#     print("outer func excuted")
#
#     return inner()
#
# outer()

# def outer():
#     x = 1
#     y = 1
#
#     def inner():
#         print("x=%s" %x)
#         print("y=%s" %y)
#
#     print(inner.__closure__)
#     return inner
#
# outer()




def index(url):
    def get():
        return urlopen(url).read()
    return get()

python = index("http://www.python.org") #返回的是get函数地址
print(python)
baidu = index("http://www.baidu.com")
print(baidu)