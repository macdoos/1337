# O(N^2) time | O(N) space | two pointers
def threeNumberSum(array, target_sum):
    array.sort()
    triplets = []
    N = len(array)

    for i in range(N - 2):
        left = i + 1
        right = N - 1
        while left < right:
            current_sum = array[i] + array[left] + array[right]
            if current_sum == target_sum:
                triplets.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif current_sum < target_sum:
                left += 1
            elif current_sum > target_sum:
                right -= 1
    return triplets

input = [12, 3, 1, 2, -6, 5, -8, 6]
target = 0
print(threeNumberSum(input, target))
