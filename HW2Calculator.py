import sys
def Adder(a, b):
    return a + b
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
def main():
    test()

if __name__ == '__main__':
    main()