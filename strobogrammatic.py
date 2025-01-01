nums = input()
res = set()  
for i in range(len(nums)):
    for j in range(len(nums)):
        for k in range(len(nums)):
            for l in range(len(nums)):
                num = nums[i] + nums[j] + nums[k] + nums[l]
                if num[0] == '0':
                    continue
                rotated = ''
                for i in range(len(num) - 1, -1, -1):  
                    digit = num[i]
                    if digit == '0':
                        rotated += '0'
                    elif digit == '1':
                        rotated += '1'
                    elif digit == '6':
                        rotated += '9'
                    elif digit == '8':
                        rotated += '8'
                    elif digit == '9':
                        rotated += '6'
                if rotated == num:
                    res.add(num)  
if res:
    print(','.join(sorted(res)))  
else:
    print(-1)
