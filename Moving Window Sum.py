from collections import deque
nums = [1, 2, 3, 4, 5, 6]
window_size = 3
d = deque(nums[:window_size], maxlen=window_size)
print(sum(d))
for i in range(window_size, len(nums)):
    d.append(nums[i])
    print(sum(d))
