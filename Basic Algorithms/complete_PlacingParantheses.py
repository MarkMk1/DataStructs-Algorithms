# Uses python3
import math

def evalt(a, op, b):
    if op == '+':
        return int(a) + int(b)
    elif op == '-':
        return int(a) - int(b)
    elif op == '*':
        return int(a) * int(b)
    else:
        assert False

def get_max_value(dataset):
    operators = []
    numbers = []
    for i in dataset:
        if i == '+' or i == '-' or i == '*':
            operators.append(i)
        if i.isdigit():
            numbers.append(int(i))
    n = len(numbers)
    if n == 1:
        return numbers[0]

    maximum_matrix = [[0 for x in range(n)] for y in range(n)]
    minimum_matrix = [[0 for x in range(n)] for y in range(n)]
    for i in range(0, n):
        minimum_matrix[i][i], maximum_matrix[i][i] = int(numbers[i]), int(numbers[i])

    for s in range(0, n):
        for i in range(0, n-s):
            j = i+s
            minimum = 10**10
            maximum = -10**10
            for k in range(i, j):
                a = evalt(maximum_matrix[i][k], operators[k], minimum_matrix[k+1][j])
                b = evalt(maximum_matrix[i][k], operators[k], maximum_matrix[k+1][j])
                c = evalt(minimum_matrix[i][k], operators[k], maximum_matrix[k+1][j])
                d = evalt(minimum_matrix[i][k], operators[k], minimum_matrix[k+1][j])
                minimum = min(minimum, a, b, c, d)
                maximum = max(maximum, a, b, c, d)
                minimum_matrix[i][j] = minimum
                maximum_matrix[i][j] = maximum
    return maximum_matrix[0][n-1]


if __name__ == "__main__":
    print(get_max_value(input()))