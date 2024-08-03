# O(N^2) time | O(N^2) space | iterative
def fourNumberSum(array, target_sum):
    pairs_sum = {}
    quads = []

    for i in range(1, len(array) - 1):
        for j in range(i + 1, len(array)):
            current_sum = array[i] + array[j]
            diff = target_sum - current_sum
            if diff in pairs_sum:
                for pair in pairs_sum[diff]:
                    quads.append(pair + [array[i], array[j]])

        for k in range(0, i):
            current_sum = array[i] + array[k]
            if current_sum not in pairs_sum:
                pairs_sum[current_sum] = [[array[k], array[i]]]
            else:
                pairs_sum[current_sum].append([array[k], array[i]])

    return quads

input = [7, 6, 4, -1, 1, 2]
target = 16
print(fourNumberSum(input, target))
