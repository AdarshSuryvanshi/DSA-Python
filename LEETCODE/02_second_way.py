print("Enter the elements of the sorted array separated by spaces:")
nums = list(map(int, input().split())) 
ans= list(set(nums))
print(list(ans))