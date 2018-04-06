# Uses python3
import sys

def get_change(m):
    div10 = 0
    div5 = 0
    count = 0
    remainder = m

    if m >= 10:
        div10 = m//10
        remainder -= (div10*10)

    if remainder >= 5:
        div5 = remainder//5
        remainder -= (div5*5)

    count += div10 + div5 + remainder
    return count

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
