def three_sum(arr, target):
    arr.sort()

    for i in range(len(arr) - 2):
        low = i + 1
        high = len(arr) - 1

        while low < high:
            triplet = arr[i] + arr[low] + arr[high]

            if triplet == target:
                return True
            elif triplet < target:
                low += 1
            else:
                high -= 1
    return False


def main():
    arr = [4, 2, 1, 5, 6, 7, 8, 9]
    target = 29

    print(f"The three values are {three_sum(arr, target)}")


if __name__ == "__main__":
    main()
