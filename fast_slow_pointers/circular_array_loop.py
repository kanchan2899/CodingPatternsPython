def next_step(pointer, value, size):
    result = (pointer + value) % size
    if result < 0:
        result += size
    return result


def is_not_cycle(inputs, prev_direction, pointer):
    curr_direction = inputs[pointer] >= 0

    if prev_direction != curr_direction or (abs(inputs[pointer] % len(inputs)) == 0):
        return True
    else:
        return False


def circular_array(inputs):
    size = len(inputs)

    for i in range(size):
        # set slow and fast pointer at  current index value
        slow = fast = i

        # set true in forward if element is positive, set false otherwise
        forward = inputs[i] > 0

        while True:
            # move slow pointer to one step
            slow = next_step(slow, inputs[slow], size)

            # if cycle is not possible, break the loop and start from next element
            if is_not_cycle(inputs, forward, slow):
                break

            # first move of fast pointer
            fast = next_step(fast, inputs[fast], size)
            # if cycle is not possible, break the loop and start from next element
            if is_not_cycle(inputs, forward, slow):
                break

            # second move of fast pointer
            fast = next_step(fast, inputs[fast], size)
            # if cycle is not possible, break the loop and start from next element
            if is_not_cycle(inputs, forward, slow):
                break

            # at any point, if fast and slow pointers meet each other, it indicates that loop is found
            if slow == fast:
                return True
    return False


def main():
    inputs = [2, 2, 2, 7, 2, -1, 2, -1, -1]

    print(circular_array(inputs))


if __name__ == "__main__":
    main()
