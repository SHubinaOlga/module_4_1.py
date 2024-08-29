import math
def divide(first, second):
    if second == 0:
        print(math.inf)
        return
    else:
        print(first / second)


result3 = divide(49, 7)
result4 = divide(15, 0)

