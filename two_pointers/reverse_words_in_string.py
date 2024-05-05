import re


def str_rev(_str, start, end):
    while start < end:
        _str[start], _str[end] = _str[end], _str[start]
        start += 1
        end -= 1


def reverse_words(strings):
    # remove extra space and strip leading/trailing spaces
    sentence = re.sub(' +', ' ', strings.strip())

    #  convert the sentence to a list of characters for in-place modification as strings are immutable
    sentence = list(sentence)
    str_len = len(sentence)

    # reverse the whole sentence first
    str_rev(sentence, 0, str_len - 1)
    start = 0

    # iterate through the sentence to find and reverse each word
    for end in range(0, str_len + 1):
        if end == str_len or sentence[end] == ' ':
            # reverse the current word
            str_rev(sentence, start, end - 1)
            # move the start pointer to the start of the next word
            start = end + 1

    return "".join(sentence)


def main():
    strings = "Hello World"
    print(reverse_words(strings))


if __name__ == "__main__":
    main()
