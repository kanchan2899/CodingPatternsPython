def sort_colors(colors):
    start, current, end = 0, 0, len(colors) - 1

    while current <= end:
        # if the current pointer is pointing to start
        if colors[current] == 0:
            # swap the values if start pointer is not pointing to start
            if colors[start] != 0:
                colors[start], colors[current] = colors[current], colors[start]

            # increment both the start and current
            current += 1
            start += 1

        # if the current pointer is pointing to current, no swapping is required, just increment current
        elif colors[current] == 1:
            current += 1

        # if the current pointer is pointing to end
        else:
            # swap the values if the end pointer is not pointing to end
            if colors[end] != 2:
                colors[current], colors[end] = colors[end], colors[current]

            # decrement the end pointer
            end -= 1


def main():
    colorss = [2, 1, 0, 1, 1, 2, 0, 1, 2, 2]
    sort_colors(colorss)
    print(colorss)


if __name__ == "__main__":
    main()
