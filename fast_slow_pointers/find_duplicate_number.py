def duplicate_number(nums):
    # initialize fast and slow pointers and make them point to first element in array
    fast = slow = nums[0]

    # traverse the array until the intersection point is found
    while True:
        # move the slow pointer using the nums[slow] flow
        slow = nums[slow]
        # move the fast pointer two times fast as the slow pointer using the nums[nums[fast]] flow
        fast = nums[nums[fast]]

        # break the loop when slow pointer becomes equal to the fast pointer
        if slow == fast:
            break

    # make the slow pointer point the starting position of an array again, point the slow pointer at start
    slow = nums[0]

    while slow != fast:
        # move the slow pointer using nums[slow] flow
        slow = nums[slow]
        # move the fast pointer slower than before i.e., move the fast pointer using nums[fast] flow
        fast = nums[fast]

    # return the fast pointer as it points the duplicate number of the array
    return fast


def main():
    nums = [1, 6, 3, 5, 5, 2, 7, 4]
    print(duplicate_number(nums))


if __name__ == "__main__":
    main()
