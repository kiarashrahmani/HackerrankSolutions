n = int(input())
arr = list(map(int, input().split()))

arr.sort(reverse=True)


i = 0
while arr[i] == arr[i+1]:
    i += 1

result = arr[i+1]
print(result)
