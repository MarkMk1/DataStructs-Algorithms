# Uses python3
import sys


def major_element(array, start, length):

    if length == 1:
        return array[start]

    if length == 0:
        return -1

    mid = length//2

    left = major_element(array, start, mid)
    right = major_element(array, mid+start, length-mid)

    if right == left:
       return left
    elif array[start:start+length].count(left) > length/2:
        return left
    elif array[start:start+length].count(right) > length/2:
        return right
    else:
        return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    x = major_element(a, 0, n)
    if x == -1:
        print(0)
    else:
        print(1)
