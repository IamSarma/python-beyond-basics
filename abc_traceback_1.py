def a():
    print("Start of a()")
    b()

def b():
    print("Start of b()")
    c()

def c():
    print("Start of c()")
    42 / 0    # This will cause a zero divide error

a()
