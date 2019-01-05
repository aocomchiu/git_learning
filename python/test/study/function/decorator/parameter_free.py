''' 多个装饰器装饰一个函数 '''



# 定义第一个装饰器
def set_func1(func):
    def wrapper1(*args,**kwargs):
        print('装饰内容开始1')
        func(*args, **kwargs)
        print('装饰内容结束1')
    return wrapper1


# 定义第二个装饰器
def set_func2(func):
    def wrapper2(*args,**kwargs):
        print('装饰内容开始2')
        func(*args, **kwargs)
        print('装饰内容结束2')
    return wrapper2

# 定义第二个装饰器
def set_func3(func):
    def wrapper3(*args,**kwargs):
        print('装饰内容开始3')
        func(*args, **kwargs)
        print('装饰内容结束3')
    return wrapper3

@set_func1
@set_func2
@set_func3
def show():
    print('Show Run....')

show()


# 结果如下:
# 装饰内容开始1
# 装饰内容开始2
# 装饰内容开始3
# Show Run....
# 装饰内容结束3
# 装饰内容结束2
# 装饰内容结束1
#
# 进程已结束，退出代码 0