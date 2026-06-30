def smart_div(func):
    def inner(a,b):
        if b==0:
            print("can not division by 2")
        else:
            return func(a,b)
        return inner    

@smart_div
def division(a,b):
    print(a/b)
print("hello world")

division(10,5)
division(10,0)