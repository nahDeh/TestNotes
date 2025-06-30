
#双指针反转字符串：
# s = ["A"," ","m","a","n",","," ","a"," ","p","l","a","n",","," ","a"," ","c","a","n","a","l",":"," ","P","a","n","a","m","a"]
# j = len(s)
# n = int(j/2)
# for i in range (0 , n):
#     a = s[i]
#     s[i] = s[len(s)-i-1]
#     s[len(s)-i-1] = a
    
# print (s)


#查询数组中心下标：
nums = [1,7,3,6,5,6]
#旧版：执行时间长，每次都要遍历获取一次总数
# class Solution(object):
#     def pivotIndex(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         leftNums = 0
#         rightNums = 0
#         for i in range(0, len(nums)):
#             leftNums = sum(nums[0:i])
#             rightNums = sum(nums[i+1:len(nums)])
#             if leftNums == rightNums:
#                 return i
#             return -1

#新版：执行时间短，先计算了右边的总数，每次循环时先减去当前下标的数，然后和左边的总数判断是否相等，不相等时再给左边的总数加上当前下标数
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftNums = 0
        rightNums = sum(nums)
        for i in range(0,len(nums)):
            rightNums -= nums[i]
            if leftNums == rightNums:
                return i
            leftNums += nums[i]
        return -1


print(Solution().pivotIndex(nums))