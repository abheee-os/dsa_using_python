arr=[1,3,4,5,7]
maximum=arr[0]
sec_maximum=float("-inf")

for num in arr:
    if num>maximum:
        
        sec_maximum=maximum
        maximum=num
        
print(maximum)
print(sec_maximum)