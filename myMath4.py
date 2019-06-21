def f1():
    if __name__ == '__main__':
        print("this code is executed directly as a program")
        print("the value of __name__ :",__name__)
    else:
        print("this code is executed in-directly by other module")
        print("the value of __name__ :",__name__)
f1()