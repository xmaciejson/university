# ZAD 1*
def subset_sums(L):
    if not L:
        return set([0])
    return set(set([x + L[0] for x in subset_sums(L[1:])]) | subset_sums(L[1:]))


def non_decreasing_sequences(N, A, B):
    if N == 0:
        return {()}
    return {(x,) + seq for x in range(A, B + 1) for seq in non_decreasing_sequences(N - 1, x, B)}

print(subset_sums([1,2,3,100]))
print(non_decreasing_sequences(3, 10, 20))
# ZAD 2
def permutacyjna_postac_normalna(word):
    mapping = {}
    counter = 1
    result = []

    for char in word:
        if char not in mapping:
            mapping[char] = counter
            counter += 1
        result.append(str(mapping[char]))

    return '-'.join(result)

print(permutacyjna_postac_normalna('tata'))