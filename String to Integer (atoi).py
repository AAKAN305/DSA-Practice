def myAtoi(s: str) -> int:
    i = 0
    n = len(s)
    sign = 1
    result = 0
    
    # Step 1: Skip leading whitespaces
    while i < n and s[i] == ' ':
        i += 1
    
    # Step 2: Check for '+' or '-'
    if i < n and (s[i] == '+' or s[i] == '-'):
        sign = -1 if s[i] == '-' else 1
        i += 1
    
    # Step 3: Convert digits to integer
    while i < n and s[i].isdigit():
        digit = int(s[i])
        result = result * 10 + digit
        i += 1
    
    # Apply sign
    result *= sign

    # Step 4: Clamp the value to 32-bit signed int range
    INT_MIN = -2**31
    INT_MAX = 2**31 - 1
    if result < INT_MIN:
        return INT_MIN
    if result > INT_MAX:
        return INT_MAX
    
    return result
