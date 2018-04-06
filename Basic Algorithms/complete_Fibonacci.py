#python3

import random
n = int(input())

def fastFib(n):
    fibArray = [0, 1]
    for i in range(2,n+1):
        fibArray.append(fibArray[i-1] + fibArray[i-2])
    if n > 1:
        return fibArray[-1]
    else:
        return n

# def slowFib(n):
#     if n <= 1:
#         return n
#     else:
#         return slowFib(n-1) + slowFib(n-2)

# for i in range(0, 10):
#     n = random.randrange(0, 30)
#     print(n)
#     fastFibProd = fastFib(n)
#     slowFibProd = slowFib(n)
#    print(fastFibProd)
#    print(slowFibProd)
#    if slowFibProd == fastFibProd:
#        print(True)
#    else:
#        print(False)
print(fastFib(n))


