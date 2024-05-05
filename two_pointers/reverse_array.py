def swap(arr, start, end):
    temp = arr[start]
    arr[start] = arr[end]
    arr[end] = temp


def reverse_array(arr):
    start = 0
    end = len(arr) - 1

    while start < end:
        swap(arr, start, end)
        start = start + 1
        end = end - 1
    return arr


def main():
    arr = [[1, 2, 3, 4, 5, 6], [1, 2, 3, 4]]

    for i in range(len(arr)):
        print(f"The array is {arr[i]}")
        print(f"The reversed array is {reverse_array(arr[i])}")
        print("**********************")


if __name__ == "__main__":
    main()
