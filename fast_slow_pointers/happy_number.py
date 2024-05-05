def is_happy(n: int):
    def sum_of_squared_digits(number: int):
        total_sum = 0
        while number > 0:
            number, digit = divmod(number, 10)
            total_sum += digit ** 2
        return total_sum

    slow_pointer = n
    fast_pointer = sum_of_squared_digits(n)

    while fast_pointer != 1 and slow_pointer != fast_pointer:
        slow_pointer = sum_of_squared_digits(slow_pointer)
        fast_pointer = sum_of_squared_digits(sum_of_squared_digits(fast_pointer))

    if fast_pointer == 1:
        return True

    return False


def main():
    inputs = [1, 5, 19, 25, 7]
    for i in range(len(inputs)):
        print(is_happy(inputs[i]))


if __name__ == "__main__":
    main()
