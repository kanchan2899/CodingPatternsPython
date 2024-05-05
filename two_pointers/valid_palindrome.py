# Solution 1: Reverse the string and then compare the reversed string with the original string.
# TC: O(n) and SC: O(n)

# Solution 2: Two Pointers, where the first pointer is at the starting element of the string, which the
# second pointer is at the end of the string. We move the two pointers towards the middle of the string
# and, at each iteration, we compare each element. The moment we encounter a nonidentical pair,
# we can return FALSE because our string can’t be a palindrome.
# TC: O(n / 2) and SC: O(1)

def is_palindrome(str):
    left = 0
    right = len(str) - 1

    while left < right:
        if str[left] != str[right]:
            return False
        left = left + 1
        right = right - 1
    return True


def main():
    strings = ["RACEACAR", "A", "ABCDEFGFEDCBA"]
    for i in range(len(strings)):
        print(f"Is {strings[i]} palindrome? {is_palindrome(strings[i])}")


if __name__ == "__main__":
    main()
