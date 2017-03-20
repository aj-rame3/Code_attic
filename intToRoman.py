class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        romanNums = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        deciNums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        
        if type(num) != type(1):
            print "Input is not a valid number"
        if not 0 < num < 3999:
            print "Input is too large"
        
        result = ""
        
        for i in range(len(deciNums)):
            count = int(num / deciNums[i])
            result += romanNums[i] * count
            num -= deciNums[i] * count
            
        return result
            
