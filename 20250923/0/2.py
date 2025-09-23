nums = [i for i in range(5, 15 + 1)]
chars = [chr(ch) for ch in range(ord('a'), ord('k')+1)]
nums[3:7] = chars[-5:]
print(nums)
print(chars)