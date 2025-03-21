def counting_sort(arr):
    n = len(arr)
    if n == 0:
        return []

    MAX = max(arr)
    MIN = min(arr)

    range_of_elements = MAX - MIN + 1
    count = [0] * range_of_elements

    for i in range(n):
        count[arr[i] - MIN] += 1

    for i in range(1, range_of_elements):
        count[i] += count[i - 1]

    sorted_arr = [0] * n
    for i in range(n - 1, -1, -1):
        sorted_arr[count[arr[i] - MIN] - 1] = arr[i]
        count[arr[i] - MIN] -= 1

    return sorted_arr