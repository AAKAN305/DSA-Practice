def intToRoman(num: int) -> str:
    # Roman numeral values with their symbols (largest → smallest)
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syms = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    
    roman = ""
    i = 0
    
    # Loop through each value
    while num > 0:
        # Subtract as many times as possible
        while num >= val[i]:
            num -= val[i]
            roman += syms[i]
        i += 1
    
    return roman


# 🔹 Testing
print(intToRoman(3749))  # Output: "MMMDCCXLIX"
print(intToRoman(58))    # Output: "LVIII"
print(intToRoman(1994))  # Output: "MCMXCIV"
