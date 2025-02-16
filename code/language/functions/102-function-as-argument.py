def world():
    return " World!"

def hello(call = world()):
    print("Hello" + call)
    
hello()