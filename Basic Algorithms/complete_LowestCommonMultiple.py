#python3

a = [int(x) for x in input().split()]

A = a[0]
B = a[1]

def LCM(A, B):
    return (A*B)//xGCD(A,B)

def GCD(A, B):
    if B == 0:
        return A
    else:
        A_prime = A % B
        return (GCD(B, A_prime))

print(int(LCM(A,B)))