# Uses python3
import sys


def get_optimal_value(capacity, weights, values):

    value = float(0.0)
    capacity = float(capacity)
    n = len(weights)

    while capacity > 0.0 and n > 0:

        current_mvp = 0
        mvp_value_unit_weight = float(values[current_mvp])/float(weights[current_mvp])
        for i in range(0, n):
            value_unit_weight = float(values[i])/float(weights[i])
            if value_unit_weight > mvp_value_unit_weight:
                current_mvp = i
                mvp_value_unit_weight = float(values[current_mvp]) / float(weights[current_mvp])

        if weights[current_mvp] > 0.0:
            if weights[current_mvp] <= capacity:
                value += values[current_mvp]
                capacity -= weights[current_mvp]
                del weights[current_mvp]
                del values[current_mvp]
                n -= 1
            else:
                value += capacity * mvp_value_unit_weight
                values[current_mvp] -= capacity * mvp_value_unit_weight
                weights[current_mvp] -= capacity
                capacity = 0.0
                break
        else:
            del weights[current_mvp]
            del values[current_mvp]
            n -= 1

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value))
