"""
from sys import stdin
# 执行速度是input()语句的4倍
a, b = map(int, stdin.readline().split())
print(a + b)

# 输入一个整数列表,第一个参数是整形，可改
nums = list(map(int, stdin.readline().split()))
print(nums)

# 初始化一个3行4列的矩阵
M1 = [[0] * 3 for _ in range(4)]
print(M1)
"""
# 格式化输出

testCase = 5
percentage = 0.66
city = "Beijing"

print("Case #%i: %.02f %s" % (testCase, percentage, city))
