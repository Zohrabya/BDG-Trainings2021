#!usr\bin\env python 3
#1
print("Input six integers:")
nums = list(map(int, input().split()))
nums.sort()
nums.reverse()

#2
print("After sorting the said ntegers:")
print(*nums)