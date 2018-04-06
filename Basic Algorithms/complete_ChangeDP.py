# Uses python3
import sys


def get_change_recursively(m, c):
    table = [0]
    min_coins = 10**3 + 1
    if m == 0:
        return table[0]

    for i in range(0, len(c)):
        if m > c[i]:
            num_coins = get_change(m - c[i], c)
            if num_coins + 1 < min_coins:
                min_coins = num_coins + 1
    return min_coins


def get_change(money, coins):
    min_coins = [0]
    for i in range(0, money):
        min_coins.append(0)

    if money == 0:
        return 0

    for m in range(1, money+1):
        min_coins[m] = 1001
        for c in range(0, len(coins)):
            if m >= coins[c]:
                cur_coins = min_coins[m-coins[c]] + 1
                if cur_coins < min_coins[m]:
                    min_coins[m] = cur_coins
    return min_coins[money]


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m, [1, 3, 4]))
