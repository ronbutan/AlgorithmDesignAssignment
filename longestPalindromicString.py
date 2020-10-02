def longestPalindrome(self, s):
    lenS = len(s)
    isOdd = 0
    if lenS > 1000:
        return s
    if lenS % 2 != 0:
        isOdd = 1
    
    mid = lenS // 2
    firstPart = s[0:mid+1]
    secondPart = s[mid+2:] if isOdd else s[mid+1:]
    secondpart = secondPart[::-1]
    for 

longestPalindrome("babad")