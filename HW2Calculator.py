import sys
def Adder(a, b):
    return a + b
def Subtracter(a,b):
    return a - b
def Multiplier(a,b):
    return a*b
def Divider(a,b):
    return a//b
def test():
    if 3 == Adder(1,2):
        print("positive integer test passed")
    else:
        print("positive integer test failed")
    if -1 == Adder(1,-2):
        print("negative and positive integer test passed")
    else:
        print("negative and positive integer test failed")
    if -3 == Adder(-1,-2):
        print("negative integer test passed")
    else:
        print("negative integer test failed")
    if 1 == Adder(1,0):
        print("zero addition passed")
    else:
        print("zero addition failed")
    if 3 == Subtracter(6,3):
        print("positive subtraction passed")
    else:
        print("positive subtraction failed")
    if 5 == Subtracter(3,-2):
        print("negative and positive subtraction test passed")
    else:
        print("negative and positive subtraction test failed")
    if -1 == Subtracter(-3,-2):
        print("negative subtration passed")
    else:
        print("negative subtraction failed")
    if 1 == Subtracter(1,0):
        print("zero subtraction passed")
    else:
        print("zero subtraction passed")
    if 300 == Multiplier(1,300):
        print("multi identity test passed")
    else:
        print("multi identity test failed")
    if 0 == Multiplier(0,99):
        print("multiplication by zero passed")
    else:
        print("multiplication by zero failed")
    if 6 == Multiplier(2,3):
        print("positive multiplication passed")
    else:
        print("positive muliplication failed")
    if -6 == Multiplier(2,-3):
        print("mixed multiplication passed")
    else:
        print("mixed multiplication failed")
    if 6 == Multiplier(-2,-3):
        print("negative multiplication passed")
    else:
        print("negative multiplication failed")
    
def main():
    test()

if __name__ == '__main__':
    main()