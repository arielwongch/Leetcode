"""
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n==0:
            return ""
        palindrome = [[0]*n for _ in range(n) ]

        longest_substring = 1
        starting_index = 0
        ending_index = 0

        for i in range(n):
            palindrome[i][i]=1

        for i in range(n):
            for j in range(i+1):
                if i == j:
                    palindrome[j][i]=1
                elif (j>i):
                    palindrome[j][i]=-1
                    continue
                else:
                    if s[i] == s[j]:
                        if(j+1 == i):
                            palindrome[j][i]=1
                        else:
                            palindrome[j][i] = palindrome[j+1][i-1]

                        if(palindrome[j][i] == 1 and i-j+1 > longest_substring):
                            longest_substring = i-j+1
                            starting_index = j
                            ending_index = i
                    else:
                        palindrome[j][i] = 0
        return s[starting_index:ending_index+1]
