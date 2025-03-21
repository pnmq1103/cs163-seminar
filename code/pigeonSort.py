def pigeonhole_sort(arr):
    MIN = min(arr)
    MAX = max(arr)
    range_size = MAX - MIN + 1

    holes = [0] * range_size

    for num in arr:
        holes[num - MIN] += 1

    index = 0
    for i in range(range_size):
        while holes[i] > 0:
            arr[index] = i + MIN
            index += 1
            holes[i] -= 1