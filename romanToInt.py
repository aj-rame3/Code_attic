class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romNum = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
        intNum = [1000, 500, 100, 50, 10, 5, 1]
        mapRomans = []
        
        if not s:
            print "String is Empty, Input a valid string"
        
        if type("s") != type(""):
            print "Input a valid string, Input looks %s" % type(s)
        
        s = s.upper()
        for letter in s:
            if not letter in romNum:
                print "S does not contain Valid Roman Numerals"
        
        for i in range(len(s)):
            each_letter = s[i]
            value = intNum[romNum.index(each_letter)]
            try:
                nextValue = intNum[romNum.index(s[i+1])]
                if nextValue > value:
                    value = value * -1
            except IndexError:
                pass
            
            mapRomans.append(value)
        
        sum = 0
        for eachRoman in mapRomans:
            sum = sum + eachRoman
        
        return sum
        
