"""
Input: s = "4193 with words"
Output: 4193
"""

import re

class Solution:
    def myAtoi(self, s: str) -> int:
        pattern = re.compile(r'\d+|\-\d+')
        pattern2 =  re.compile(r'\d+')
        
        d = 0
        for i in pattern2.search(s).group():
            for j in range(10):
                if str(j)==i:
                    d = (d*10)+j
                    
        if pattern.search(s).group()==pattern2.search(s).group():
            return d
        else:
            d = 0-d
            return d
        return 0