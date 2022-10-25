class Solution:
    def romanToInt(self, s: str) -> int:
        allowed_s ="IVXLCDM"
        s = s.upper()
        val = {}
        if all(j in allowed_s for j in s) == False or len(s) < 1 or len(s) > 15 or all(s.count(i) >= 4 for i in s) == True:
            print("enter valid roman numerals")
        else:
            for x in s:
                if x == 'I':
                    if 'IV' in s:
                        val['h'] = 4
                    elif 'IX' in s:
                        val['i'] = 9
                    else:
                        val['a'] = 1*s.count(x)
                elif x == 'V':
                    if 'IV' in s:
                        val['h'] = 4
                    else:
                        val['b'] = 5*s.count(x)
                elif x == 'X':
                    if 'XIX' in s or 'IX' in s:
                        t = s.replace('CM', '')
                        t = t.replace('CD', '')
                        t = t.replace('XC', '')
                        t = t.replace('XL', '')
                        t = t.replace('IX', '')
                        t = t.replace('IV', '')

                        val['c'] = 10*t.count(x)
                        val['i'] = 9
                    elif 'XL' in s:
                        val['j'] = 40
                    elif 'XC' in s:
                        val['k'] = 90
                    else:
                        val['c'] = 10*s.count(x)
                elif x == 'L':
                    if 'XL' in s:
                        val['j'] = 40
                    else:
                        val['d'] = 50*s.count(x)
                elif x == 'C':
                    if 'CXC' in s or 'XC' in s:
                        t = s.replace('CM', '')
                        t = t.replace('CD', '')
                        t = t.replace('XC', '')
                        t = t.replace('XL', '')
                        t = t.replace('IX', '')
                        t = t.replace('IV', '')

                        val['e'] = 100*t.count(x)
                        val['k'] = 90
                    elif 'CD' in s:
                        val['l'] = 400
                    elif 'CM' in s:
                        val['m'] = 900
                    else:
                        val['e'] = 100*s.count(x)
                elif x == 'D':
                    if 'CD' in s:
                        val['l'] = 400
                    else:
                        val['f'] = 500*s.count(x)
                elif x == 'M':
                    if 'MCM' in s or 'CM' in s:
                        t = s.replace('CM', '')
                        t = t.replace('CD', '')
                        t = t.replace('XC', '')
                        t = t.replace('XL', '')
                        t = t.replace('IX', '')
                        t = t.replace('IV', '')
                        
                        val['g'] = 1000*t.count(x)
                        val['m'] = 900
                    else:
                        val['g'] = 1000*s.count(x)
                else:
                    print("Cannot convert this roman numeral")
        res = sum(val.values())
        return(res)
   
e1 = Solution()
print(e1.romanToInt("III"), "\n")

e2 = Solution()
print(e2.romanToInt("LVIII"), "\n")

e3 = Solution()
print(e3.romanToInt("MCMXCIV"))

e4 = Solution()
print(e4.romanToInt("MMCCCXCIX"))

e5 = Solution()
print(e5.romanToInt("MMMCDXC"))

e6 = Solution()
print(e6.romanToInt("MMMCDXXIX"))