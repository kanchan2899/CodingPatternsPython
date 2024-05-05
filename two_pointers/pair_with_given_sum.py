from typing import Dict
from itertools import combinations


def pair(arr, target):
    result = []
    for x in range(len(arr)):
        for y in range(x + 1, len(arr)):
            if arr[x] + arr[y] == target:
                result.append((arr[x], arr[y]))
    return result


def pair1(arr, target):
    result = []
    while arr:
        num = arr.pop()
        diff = target - num

        if diff in arr:
            result.append((diff, num))
    result.reverse()
    return result


def pair2(arr, target):
    seen = set()
    result = []
    for num in arr:
        complement = target - num
        if complement in seen:
            result.append((num, complement))
        seen.add(num)

    return result


def pair3(arr, target):
    pairs = []
    arr.sort()
    left = 0
    right = len(arr) - 1

    while left < right:
        if arr[left] + arr[right] == target:
            pairs.append((arr[left], arr[right]))
            left += 1
            right -= 1
        elif arr[left] + arr[right] < target:
            left += 1
        else:
            right -= 1
    return pairs


def main():
    arr = [4, 1, 5, 2, 3, 6]
    target = 8
    print(f"Pair with given sum is {pair(arr, target)}")
    print(f"Pair with given sum is {pair1(arr, target)}")
    print(f"Pair with given sum is {pair2([4, 1, 5, 2, 3, 6], target)}")
    print(f"Pair with given sum is {pair3([4, 1, 5, 2, 3, 6], target)}")


if __name__ == "__main__":
    main()
