# Modify the following code so that it outputs the correct answer.

import math
def foo(a):
    return math.pow(a,3)+2*math.pow(a,2)+a
def is_Root(a):
    if foo(a)==0:
        return False
    else:
        return True

while(True):
    x = int(input("Please input a test value:"))

    print(is_Root(x))
