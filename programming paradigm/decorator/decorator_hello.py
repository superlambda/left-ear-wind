def hello(fn):
    def wrapper():
        print ("hello, %s" % fn.__name__)
        fn()
        print ("goodbye, %s" % fn.__name__)
    return wrapper
 
@hello
def Yingjie_Liu():
    print ("i am Yingjie Liu")
 
Yingjie_Liu()
