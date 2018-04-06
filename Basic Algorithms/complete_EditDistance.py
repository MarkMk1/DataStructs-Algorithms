# Uses python3

def edit_distance(f, s):

    distance_matrix = [[0 for x in range(len(f)+1)] for y in range(len(s)+1)]
    for i in range(len(f)):
        distance_matrix[0][i+1] = i + 1
    for j in range(len(s)):
        distance_matrix[j+1][0] = j + 1

    for i in range(1, len(f)+1):
        for j in range(1, len(s)+1):
            match_mismatch = 0
            if f[i-1] != s[j-1]:
                match_mismatch = 1
            distance_matrix[j][i] = min(distance_matrix[j-1][i-1] + match_mismatch,
                                        distance_matrix[j][i-1] + 1, distance_matrix[j-1][i] + 1)

    return distance_matrix[-1][-1]

if __name__ == "__main__":
    print(edit_distance(input(), input()))