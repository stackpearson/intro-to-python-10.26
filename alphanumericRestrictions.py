def csAlphanumericRestriction(input_str):
    if input_str.isdecimal():
        return True

    elif input_str.isalpha():
        return True
    
    else:
        return False

print(csAlphanumericRestriction('12345'))
print(csAlphanumericRestriction('abcdefg'))
print(csAlphanumericRestriction('abc123'))