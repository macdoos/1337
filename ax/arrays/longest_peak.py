# O(N) time | O(1) space | two pointers
def longestPeak(array):
    longest_peak_len = 0
    i = 1

    while i < len(array) - 1:
        is_peak = array[i - 1] < array[i] and array[i] > array[i + 1]
        if not is_peak:
            i += 1
            continue

        left = i - 2
        while left >= 0 and array[left] < array[left + 1]:
            left -= 1

        right = i + 2
        while right < len(array) and array[right] < array[right - 1]:
            right += 1

        current_peak_len = right - left - 1
        longest_peak_len = max(longest_peak_len, current_peak_len)
        i = right

    return longest_peak_len

input = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
print(longestPeak(input))
