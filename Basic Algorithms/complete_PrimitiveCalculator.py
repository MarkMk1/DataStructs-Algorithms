# Uses python3
import sys
import math as mm


def optimal_sequence(n):
    cost = []
    parent_pos = []
    true_parent = []

    for f in range(0, n):
        cost.append(0)

    if n == 1:
        cost.append(0)
        return cost, 1

    for i in range(1, n):
        cur_parent = i - 1
        min_cost = cost[i - 1]
        if (i+1) % 3 == 0:
            if cost[i//3] < min_cost:
                min_cost = cost[i//3]
                cur_parent = i//3
        if (i+1) % 2 == 0:
            if cost[i//2] < min_cost:
                min_cost = cost[i//2]
                cur_parent = i//2
        cost[i] = min_cost + 1
        parent_pos.append(cur_parent)

    parent_pos = [0] + [1 + pos for pos in parent_pos]
    true_parent.append(n)
    parent_backcheck = parent_pos[-1]

    for i in range(0, cost[-1]):
        true_parent.append(parent_backcheck)
        parent_backcheck = parent_pos[parent_backcheck-1]
    return cost, reversed(true_parent)


input = sys.stdin.read()
n = int(input)
sequence, true_parent = optimal_sequence(n)
print(sequence[-1])
if true_parent != 1:
    for x in true_parent:
        print(x, end=' ')
else:
    print(1)
