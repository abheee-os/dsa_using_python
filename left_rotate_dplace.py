arr=[1,2,3,4,5,6,7]
d=3
n=len(arr)

temp=[0]*d

for i in range(d):
    temp[i]=arr[i]

for i in range(d,n):
    arr[i-d]=arr[i]

for i in range((n-d),n):
    arr[i]=temp[i-(n-d)]

print(arr)
