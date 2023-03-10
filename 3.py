def is_palindrome(s):
    s = s.lower().replace(" ", "")
    rev_s = s[::-1]
    if s == rev_s:
        return True
    else:
        return False
