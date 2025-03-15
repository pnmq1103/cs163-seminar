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
