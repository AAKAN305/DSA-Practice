from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
    if not strs:
        return ""
    
    # Start with the first word as the prefix
    prefix = strs[0]
    
    # Compare with every other word
    for word in strs[1:]:
        # Shrink prefix until it matches the beginning of word
        while not word.startswith(prefix):
            prefix = prefix[:-1]  # remove last character
            if prefix == "":
                return ""
    
    return prefix


# 🔹 Testing
print(longestCommonPrefix(["flower","flow","flight"]))  # Output: "fl"
print(longestCommonPrefix(["dog","racecar","car"]))     # Output: ""
