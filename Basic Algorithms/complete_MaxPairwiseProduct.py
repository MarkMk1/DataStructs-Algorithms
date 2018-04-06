# Uses python3
n = int(input())
a = [int(x) for x in input().split()]

init1 = 0
init2 = 0

for i in range(n):
    if a[i] > init1 and init1 <= init2:
        init1 = a[i]
    elif a[i] > init2:
        init2 = a[i]

product = init1 * init2
print(product)
