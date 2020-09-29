# Find the palindrome
def is_palindrome(a_string):

    if len(a_string) <= 1:
        return True
    if a_string[0] == a_string[len(a_string) - 1]:
        return is_palindrome(a_string[1:-1])
    else:
        return False
a_string = input("Please enter a number: ")
if is_palindrome(a_string):
    print(a_string,"This is a palindrome")
else:
    print('This is not a palindrome')

