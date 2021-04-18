""" Geeks for Geeks Problem of the day

Given a number N, generate bit patterns from 0 to 2^N-1 such that successive patterns differ by one bit. 
--------------
Example 1:
--------------
Input:
N = 2
Output: 
00 01 11 10
Explanation: 
00 and 01 differ by one bit.
01 and 11 differ by one bit.
11 and 10 also differ by one bit.
--------------
Example 2:
--------------
Input:
N=3
Output:
000 001 011 010 110 111 101 100
Explanation:
000 and 001 differ by one bit.
001 and 011 differ by one bit.
011 and 010 differ by one bit.
Similarly, every successive pattern 
differs by one bit.
--------------
Your task:
You don't need to read input or print anything. 
Your task is to complete the function graycode() 
which takes an integer N as input and returns a list of patterns.
--------------
Expected Time Complexity: O(2^n)
Expected Auxiliary Space: O(2^n)
--------------
Constraints :
1<=N<=16
"""

class Solution:
    def graycode(self,n):
        #code here
        gray = []
        for i in range(0, 1<<n):
            gray.append(bin(i^(i>>1))[2:][-n:].zfill(n))
        return gray
      
      
import math
def main():
    T=int(input())
    while T>0:
        n=int(input())
        ob=Solution()
        l=ob.graycode(n)
        for x in l:
            print(x,end=" ")
        print()
        T=-1
    
if __name__=="__main__":
    main()
