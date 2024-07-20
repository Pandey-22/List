N=int(input("enter the size of list:-"))
arr=[]
for i in range(N):
    element=int(input(f"Enter element:-"))
    arr.append(element)
count={}
duplicates=[]
for number in arr:
    if number in count:
        count[number]+=1
    else:
        count[number]=1
for number in count:
    if count[number]>1:
        duplicates.append(number)
for duplicate in duplicates:
    print(duplicate, end=" ")