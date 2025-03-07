def is_palindrome(s):
    s = cleaner(s)
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True



def cleaner(s):
    cleaned = ""
    for ss in s:
        if(ss.isalnum()):
            cleaned += ss.lower()
    return cleaned

test_input = "A man, a plan, a canal: Panama"
result = is_palindrome(test_input)
print(result)  