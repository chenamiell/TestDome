def is_palindrome(word):
    rev = ''.join(reversed(word))
    if rev.lower() == word.lower():
        return True
    return False


print(is_palindrome('Deleveled'))