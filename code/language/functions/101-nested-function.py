def hello():
    def world():
        print("Hello world")
    return world


world = hello()

world()