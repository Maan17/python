class MyException(Exception):
    def __init__(self,message='Invalid Age for Booking'):
        self.message=message
age=int(input("Enter Age"))
try:
    if (age>100):
        raise MyException()
    else:
        print("Valid Age for Booking")
except Exception as e:
    print(e.message)
