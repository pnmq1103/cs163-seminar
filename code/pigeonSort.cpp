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
