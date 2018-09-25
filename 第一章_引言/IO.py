from sys import stdin

# 执行速度是input()语句的4倍
a, b = map(int, stdin.readline().split())
print(a + b)

# 输入一个整数列表,第一个参数是整形，可改
nums = list(map(int, stdin.readline().split()))
print(nums)
