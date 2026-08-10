arr=[2,3,5,7,8]

for i in range(len(arr)-1):
    if(arr[i]>arr[i+1]):
        print("array is not sorted")
        break

else:
    print("Array is sorted")

    