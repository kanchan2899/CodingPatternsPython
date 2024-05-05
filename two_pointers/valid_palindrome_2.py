def valid_palindrome_util(s, i, j):
    while i < j:
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            return False
    return True


def valid_palindrome(s):
    i, j = 0, len(s) - 1

    while i < j:
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            return valid_palindrome_util(s, i + 1, j) or valid_palindrome_util(s, i, j - 1)
    return True


def main():
    s = "ABCREWQCBA"
    print(valid_palindrome(s))


if __name__ == "__main__":
    main()