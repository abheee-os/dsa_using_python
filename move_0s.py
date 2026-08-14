#BRUTE FORCE#
arr=[1,0,3,4,0,5]
temp=[0]*len(arr) #temp=[]
j=0
for i in range(len(arr)):
    if(arr[i]!=0):
        temp[j]=arr[i] # temp.append(num)
        j=j+1

for i in range(0,len(temp)):
    arr[i]=temp[i]

for i in range(len(temp),len(arr)):
    arr[i]=0

print(temp)

#optimal
# arr = [1, 0, 3, 4, 0, 5]

# i = 0

# for j in range(len(arr)):
#     if arr[j] != 0:
#         arr[i], arr[j] = arr[j], arr[i]
#         i += 1

# print(arr)