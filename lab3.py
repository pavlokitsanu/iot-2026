def in_asc_order(arr, n):
    return all(
        arr[i] <= arr[i + 1] for i in range(n - 1)
    )

if __name__ == "__main__":
    tests = [
        ([1, 2, 4, 7, 19], 5),
        ([1, 2, 3, 4, 5], 5),
        ([1, 6, 10, 18, 2, 4, 20], 7),
        ([9, 8, 7, 6, 5, 4, 3, 2, 1], 9),
    ]
    for arr, n in tests:
        result = in_asc_order(arr, n)
        print(f"in_asc_order({arr}, {n}) -> {in_asc_order(arr, n)}")