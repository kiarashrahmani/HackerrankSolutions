n = int(input())  # Input: Length of the array
arr = list(map(int, input().split()))  # Input: Array elements

arr.sort(reverse=True)  # Sort the array in descending order

i = 0  # Counter variable
while arr[i] == arr[i+1]:  # Find the first unique element
    i += 1

result = arr[i+1]  # Next unique element after the repeated ones
print(result)  # Output: Result
