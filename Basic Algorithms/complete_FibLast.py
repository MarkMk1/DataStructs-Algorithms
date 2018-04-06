#python3

n = int(input())

def lastFib(n):
    fibArray = [0,1]
    for i in range(2,n+1):
        fibArray.append((fibArray[i-1] + fibArray[i-2])%10)
    return fibArray[-1]

print(lastFib(n))