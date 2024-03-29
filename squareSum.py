"""
Given a non negative integer A,

following code tries to find all pair of integers (a, b) such that

            a and b are positive integers
            a <= b, and
            a2 + b2 = A.
            0 <= A <= 100000
However, the code has a small bug. Correct the bug and submit the code.
"""
# This is first approach

class Solution:
    def squareSum(self, A):
        ans = []
        a = 0
        while a * a < A:
            b = 0
            while b * b < A:
                if a * a + b * b == A:
                    newEntry = [a, b]
                    ans.append(newEntry)
                b += 1
            a += 1
        if ans == []:
            return ans
        else:
            for i in ans:
                return i


s = Solution()
print(s.squareSum(2))

# This is second approach

class Solution:
	def squareSum(self, A):
		ans = []
		a = 1
		while a * a < A:
			b = a
			while b * b < A:
				if a * a + b * b == A:
					newEntry = [a, b]
					ans.append(newEntry)
				b += 1
				
			a += 1
		return ans