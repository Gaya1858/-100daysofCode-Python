def loggin_decorator(function):
    def wrapper(*args,**kwargs):
        print(f"you have called {function.__name__}{args}")
        result =function(args[0],args[1],args[2])
        print(f"It returned: {result}")
    return wrapper

@loggin_decorator
def a_function(a,b,c):
    return a+b+c

a_function(10,201938,3000)