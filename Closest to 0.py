n = int(input())
arr = list(map(int, input().split()))

closest = arr[0]
for num in arr:
    if abs(num) < abs(closest) or (abs(num) == abs(closest) and num > closest):
        closest = num

print(closest)
