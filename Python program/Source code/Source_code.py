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
    print("\n=== MENU SẮP XẾP ===")
    print("1. Counting Sort")
    print("2. Heap Sort")
    print("3. Odd-Even Sort")
    print("4. Pigeonhole Sort")
    print("5. Thoát")

def main():
    # Nhập mảng
    try:
        n = int(input("Nhập số lượng phần tử: "))
        if n < 0:
            print("Số lượng phần tử không thể âm!")
            return
        arr = []
        for i in range(n):
            arr.append(int(input(f"Nhập phần tử thứ {i+1}: ")))
        print("Mảng ban đầu:", arr)

        while True:
            display_menu()
            choice = input("Chọn thuật toán (1-5): ")

            # Tạo bản sao mảng để không thay đổi mảng gốc
            arr_copy = arr.copy()
            sorted_arr = []

            if choice == '1':
                sorted_arr = counting_sort(arr_copy)
                print("Mảng sau khi sắp xếp bằng Counting Sort:", sorted_arr)
            elif choice == '2':
                sorted_arr = heap_sort(arr_copy)
                print("Mảng sau khi sắp xếp bằng Heap Sort:", sorted_arr)
            elif choice == '3':
                sorted_arr = odd_even_sort(arr_copy)
                print("Mảng sau khi sắp xếp bằng Odd-Even Sort:", sorted_arr)
            elif choice == '4':
                sorted_arr = pigeonhole_sort(arr_copy)
                print("Mảng sau khi sắp xếp bằng Pigeonhole Sort:", sorted_arr)
            elif choice == '5':
                print("Chương trình đã kết thúc!")
                break
            else:
                print("Lựa chọn không hợp lệ! Vui lòng chọn lại.")
    except ValueError:
        print("Lỗi: Vui lòng chỉ nhập số nguyên!")

if __name__ == "__main__":
    main()
# Chương trình sắp xếp mảng số nguyên bằng 4 thuật toán: Counting Sort, Heap Sort, Odd-Even Sort, Pigeonhole Sort.
# Hướng dẫn sử dụng:
# 1. Nhập số lượng phần tử (n) của mảng (phải là số nguyên không âm).
# 2. Nhập lần lượt n số nguyên để tạo mảng.
# 3. Chọn thuật toán sắp xếp từ menu bằng cách nhập số từ 1 đến 5:
#    - 1: Sắp xếp bằng Counting Sort
#    - 2: Sắp xếp bằng Heap Sort
#    - 3: Sắp xếp bằng Odd-Even Sort
#    - 4: Sắp xếp bằng Pigeonhole Sort
#    - 5: Thoát chương trình
# 4. Sau khi chọn, chương trình sẽ hiển thị mảng đã sắp xếp.
# 5. Có thể chọn lại thuật toán khác hoặc thoát.
# Lưu ý: Nhập sai định dạng (ví dụ: chữ thay vì số) sẽ gây lỗi và hiển thị thông báo.