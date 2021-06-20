while(True):
    try:
        x=int(input("input value for x:\n"))
        assert(x>500),"Value must be greater than 500"
        y=int(input("input value of y:\n"))
        z=x/y
        print("Result is:"+str(z))
    except(ZeroDivisionError,ValueError,AssertionError) as v
    :
        print(v)
    else:
        break

def square(x):
    return x+x

assert square(10)==100
