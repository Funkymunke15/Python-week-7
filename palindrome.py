# Davis Arita
# 10/12/2022
# CS 131 Exercise 7 part B
# determines if a word is a palindrome

def main():
    test_case = input("Enter a string: ")
    if isPalindrome(test_case):
        print("That's a palindrome.")
    else:
        print("That isn't a palindrome.")


def isPalindrome(string):
    return string == string[::-1]


main()
