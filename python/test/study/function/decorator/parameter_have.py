import time, random


def auth(func):
    def deco():
        name=input('name: ')
        password=input('password: ')
        if name == '123' and password == '123':
            print('login successful')
            func() #wrapper()
        else:
            print('login err')
    return deco


def timmer(func):
    def wrapper():
        start_time = time.time()
        func()
        stop_time=time.time()
        print('run time is %s' %(stop_time-start_time))

    return wrapper



@auth #index = auth(timer(index))
@timmer #index = timmer(index)

def index():
    time.sleep(1)
    print("welecome to index page")

index()