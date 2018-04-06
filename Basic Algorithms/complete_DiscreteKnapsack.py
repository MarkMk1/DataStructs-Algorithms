# Uses python3
import sys

# W = Weight capacity, weights = array of values
def optimal_weight(W, weights):
    # No. of weights, or last index + 1
    no_items = len(weights)
    # Initialization of (no_items * weight capacity) matrix
    values = [[0 for x in range(no_items+1)] for y in range(W+1)]
    # Looping through items considered
    for i in range(1, no_items+1):
        # Looping through weight capacities
        for w in range(1, W+1):
            # Current value (starting at 1,1) is set to what it would be with one less item considered
            values[w][i] = values[w][i - 1]
            # Check if weight of most recently considered item is of the weight allowed.
            if weights[i-1] <= w:
                # Set val to value up one row, and to left by number of spaces of current item.
                # Add the value of current item.
                val = values[w - weights[i-1]][i-1] + weights[i-1]
                # Gets max of set.
                if values[w][i] < val:
                    values[w][i] = val
    return values[W][no_items]

if __name__ == '__main__':
    input = sys.stdin.read()
    # W is weight capacity, n is number of items
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
