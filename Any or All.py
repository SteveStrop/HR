N = 5
nums = "12 19 5 -13 14".split()
print(all([int(n) > 0 for n in nums]) and any([n == n[::-1] for n in nums]))
