# Uses python3
import sys


def binary_search(a, x):
    return binary_search_recursive(a, x, 0, len(a))


def binary_search_recursive(a, x, l, r):
    left, right = l, r
    mid = (left + right)//2

    if x == a[mid]:
        return mid
    elif mid+1 < len(a)-1 and x == a[mid+1]:
        return mid+1
    elif left == mid or right == mid:
        return -1
    elif x > a[mid]:
        left = mid
    elif x < a[mid]:
        right = mid

    return binary_search_recursive(a, x, left, right)




if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        print(binary_search(a, x), end = ' ')
