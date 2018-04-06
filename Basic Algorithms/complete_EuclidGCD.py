#python3
a = [int(x) for x in input().split()]

A = a[0]
B = a[1]

def EuclidGCD(A, B):
    if B == 0:
        return(A)
    else:
        A_prime = A%B
        return(EuclidGCD(B, A_prime))

print(EuclidGCD(A, B))