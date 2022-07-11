# Uses python3
'''
The edit distance between two strings is the minimum number of operations (insertions, deletions, and
substitutions of symbols) to transform one string into another. It is a measure of similarity of two strings.
Edit distance has applications, for example, in computational biology, natural language processing, and spell
checking. Your goal in this problem is to compute the edit distance between two strings.

The last column of an optimal alignment is either
an insertion
a deletion
a mismatch
or a match
'''

def edit_distance(s, t):
    #both s and t are string in type
    source_length = len(s)
    target_length = len(t)
    distance_matrix = [[0] * (target_length + 1) for i in range(source_length + 1)]
    # Becareful we cannot do initialization in thise [[0] * 5] *5 , it will create a copy of same array of the same list
    # so when you modify one of them they all change
    for i in range(source_length + 1):
        distance_matrix[i][0] = i

    for j in range(target_length + 1):
        distance_matrix[0][j] = j

    for j in range(1, target_length + 1):
        for i in range(1, source_length + 1) :
            insertion = distance_matrix[i][j-1] + 1
            deletion = distance_matrix[i-1][j] + 1
            match = distance_matrix[i-1][j-1]
            mismatch = distance_matrix[i-1][j-1] + 1
            if s[i-1] == t[j-1]:
                distance_matrix[i][j] = min(insertion, deletion, match)

            if s[i-1] != t[j-1]:
                distance_matrix[i][j] = min(insertion, deletion, mismatch)

    return distance_matrix[source_length][target_length]


if __name__ == "__main__":
    print(edit_distance(input(), input()))