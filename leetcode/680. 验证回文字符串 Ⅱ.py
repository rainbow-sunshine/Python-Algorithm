# 给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。
#
# 示例 1:
#
# 输入: "aba"
# 输出: True
# 示例 2:
#
# 输入: "abca"
# 输出: True
# 解释: 你可以删除c字符。
# 注意:
#
# 字符串只包含从 a-z 的小写字母。字符串的最大长度是50000。
"""
思路：前后两个指针往中间走，相等就跳过，不相等就跳过然后取个或。

"""
class Solution:
    def validPalindrome(self, s: str) -> bool:
        left,right = 0 , len(s)-1
        flag = 0
        while left < right:
            if s[left] == s[right]:
                left +=1
                right -= 1
            else:
                return self.com(s,left+1,right) or self.com(s,left,right-1)
        return True

    def com(self,s,left,right):
        while left <right:
            if s[left] != s[right]:
                return False
            left +=1
            right -=1
        return True


a = Solution()
b =a.validPalindrome("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga")

print(b)