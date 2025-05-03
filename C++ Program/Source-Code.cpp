#include <iostream>
#include <vector>
#include <algorithm>

std::vector<int> countingSort(const std::vector<int>& arr) {
    int n = arr.size();
    int MAX = arr[0], MIN = arr[0];

    for (int i = 0; i < n; ++i) {
        MAX = std::max(MAX, arr[i]);
        MIN = std::min(MIN, arr[i]);
    }

    int range = MAX - MIN + 1;
    std::vector<int> count(range, 0);

    for (int i = 0; i < n; ++i)
        ++count[arr[i] - MIN];
    for (int i = 1; i < range; ++i)
        count[i] += count[i - 1];

    std::vector<int> sorted(n);

    for (int i = n - 1; i >= 0; --i) {
        --count[arr[i] - MIN];
        sorted[count[arr[i] - MIN]] = arr[i];
    }

    return sorted;
}

void heapify(std::vector<int>& arr, int i, int n) {
    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;

    if (left < n && arr[left] > arr[largest])
        largest = left;
    if (right < n && arr[right] > arr[largest])
        largest = right;

    if (largest != i) {
        std::swap(arr[i], arr[largest]);
        heapify(arr, largest, n);
    }
}

void heapSort(std::vector<int>& arr) {
    int n = arr.size();
    for (int i = n / 2 - 1; i >= 0; --i)
        heapify(arr, i, n);
    for (int i = n - 1; i > 0; --i) {
        std::swap(arr[0], arr[i]);
        heapify(arr, 0, i);
    }
}

void oddEvenSort(int arr[], int n) {
    bool isSorted = false;
    while (!isSorted) {
        isSorted = true;
        for (int i = 1; i < n - 1; i += 2) {
            if (arr[i] > arr[i + 1]) {
                std::swap(arr[i], arr[i + 1]);
                isSorted = false;
            }
        }
        for (int i = 0; i < n - 1; i += 2) {
            if (arr[i] > arr[i + 1]) {
                std::swap(arr[i], arr[i + 1]);
                isSorted = false;
            }
        }
    }
}

void pigeonholeSort(int arr[], int n) {
    int MIN = arr[0], MAX = arr[0];

    for (int i = 1; i < n; i++) {
        MIN = std::min(MIN, arr[i]);
        MAX = std::max(MAX, arr[i]);
    }

    int range = MAX - MIN + 1;
    std::vector<int> holes(range, 0);

    for (int i = 0; i < n; i++)
        ++holes[arr[i] - MIN];

    int index = 0;
    for (int i = 0; i < range; i++) {
        while (holes[i]--) {
            arr[index] = i + MIN;
            ++index;
        }
    }
}


int main() {
    int n;
    std::cout << "Enter the number of elements: ";
    std::cin >> n;

    std::vector<int> vec(n);
    int* arr = new int[n];
    std::cout << "Enter " << n << " elements: ";
    for (int i = 0; i < n; ++i) {
        std::cin >> vec[i];
        arr[i] = vec[i];
    }

    while (true) {
        std::cout << "\n=== SORTING MENU ===\n";
        std::cout << "1. Sort using Counting Sort\n";
        std::cout << "2. Sort using Heap Sort\n";
        std::cout << "3. Sort using Odd-Even Sort\n";
        std::cout << "4. Sort using Pigeonhole Sort\n";
        std::cout << "5. Exit the program\n";
        std::cout << "Choose (1-5): ";

        int choice;
        std::cin >> choice;

        if (choice == 5) break;

        std::vector<int> vecCopy = vec;
        int* arrCopy = new int[n];
        for (int i = 0; i < n; ++i) arrCopy[i] = arr[i];

        switch (choice) {
        case 1: {
            std::vector<int> sorted = countingSort(vecCopy);
            std::cout << "Result (Counting Sort): ";
            for (int x : sorted) std::cout << x << " ";
            break;
        }
        case 2: {
            heapSort(vecCopy);
            std::cout << "Result (Heap Sort): ";
            for (int x : vecCopy) std::cout << x << " ";
            break;
        }
        case 3: {
            oddEvenSort(arrCopy, n);
            std::cout << "Result (Odd-Even Sort): ";
            for (int i = 0; i < n; ++i) std::cout << arrCopy[i] << " ";
            break;
        }
        case 4: {
            pigeonholeSort(arrCopy, n);
            std::cout << "Result (Pigeonhole Sort): ";
            for (int i = 0; i < n; ++i) std::cout << arrCopy[i] << " ";
            break;
        }
        default:
            std::cout << "Invalid choice!\n";
        }
        std::cout << std::endl;
        delete[] arrCopy;
    }

    delete[] arr;
    return 0;
}

/*
Program to sort an array of integers using 4 algorithms: Counting Sort, Heap Sort, Odd-Even Sort, Pigeonhole Sort.
Usage Guide:

1. Enter the number of elements (n) in the array (must be a non-negative integer).
2. Enter n integers to create the array.
3. Choose a sorting algorithm from the menu by entering a number from 1 to 5:
   - 1: Sort using Counting Sort
   - 2: Sort using Heap Sort
   - 3: Sort using Odd-Even Sort
   - 4: Sort using Pigeonhole Sort
   - 5: Exit the program
After selecting, the program will display the sorted array.
4. You can choose another algorithm or exit.
Note: Entering incorrect formats (e.g., letters instead of numbers) will cause errors and display a message.
*/