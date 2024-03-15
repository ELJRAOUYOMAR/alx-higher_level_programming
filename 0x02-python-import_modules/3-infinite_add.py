#!/usr/bin/python3
if __name__ == "__main__":
    """ program that prints the result of the addition of all arguments
    The output should be the result of the addition of all arguments, followed by a new line
    You can cast arguments into integers by using int() (you can assume that all arguments can be casted into integers)
    Your code should not be executed when imported
    """
    import sys
    addition_total = 0
    for i in range(len(sys.argv) - 1):
        addition_total += int(sys.argv[i + 1])
    print("{}".format(addition_total))
    
        