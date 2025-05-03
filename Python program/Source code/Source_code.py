# Program to sort an integer array using 4 algorithms: Counting Sort, Heap Sort, Odd-Even Sort, Pigeonhole Sort.
# Instructions:
# 1. Enter the number of elements (n) for the array (must be a non-negative integer).
# 2. Enter n integers one by one to create the array.
# 3. Choose a sorting algorithm from the menu by entering a number from 1 to 5:
#    - 1: Sort using Counting Sort
#    - 2: Sort using Heap Sort
#    - 3: Sort using Odd-Even Sort
#    - 4: Sort using Pigeonhole Sort
#    - 5: Exit the program
# 4. After selection, the program will display the sorted array.
# 5. You can choose another algorithm or exit.
# Note: Entering incorrect formats (e.g., letters instead of numbers) will cause an error and display a message.

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

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    return arr

def odd_even_sort(arr):
    n = len(arr)
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(1, n - 1, 2):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = False
        for i in range(0, n - 1, 2):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = False
    return arr

def pigeonhole_sort(arr):
    if not arr:
        return arr
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
    return arr

def display_menu():
    print("\n=== SORTING MENU ===")
    print("1. Counting Sort")
    print("2. Heap Sort")
    print("3. Odd-Even Sort")
    print("4. Pigeonhole Sort")
    print("5. Exit")

def main():
    # Input array
    try:
        n = int(input("Enter the number of elements: "))
        if n < 0:
            print("Number of elements cannot be negative!")
            return
        arr = []
        for i in range(n):
            arr.append(int(input(f"Enter element {i+1}: ")))
        print("Original array:", arr)

        while True:
            display_menu()
            choice = input("Choose an algorithm (1-5): ")

            # Create a copy of the array to preserve the original
            arr_copy = arr.copy()
            sorted_arr = []

            if choice == '1':
                sorted_arr = counting_sort(arr_copy)
                print("Array sorted by Counting Sort:", sorted_arr)
            elif choice == '2':
                sorted_arr = heap_sort(arr_copy)
                print("Array sorted by Heap Sort:", sorted_arr)
            elif choice == '3':
                sorted_arr = odd_even_sort(arr_copy)
                print("Array sorted by Odd-Even Sort:", sorted_arr)
            elif choice == '4':
                sorted_arr = pigeonhole_sort(arr_copy)
                print("Array sorted by Pigeonhole Sort:", sorted_arr)
            elif choice == '5':
                print("Program terminated!")
                break
            else:
                print("Invalid choice! Please choose again.")
    except ValueError:
        print("Error: Please enter integers only!")

if __name__ == "__main__":
    main()