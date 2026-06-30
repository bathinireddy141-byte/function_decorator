def change_case(func):
    def inner(name):
        return func("hi"+name.upper())

        return inner
    
@change_case
def display(name):
    print(name)

display=print("sai")
display=print("prakash")
display=print("reddyy")