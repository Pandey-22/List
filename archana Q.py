# a=[[1,2,3,0],[4,5,6],[0,[9,8,7]],[5,[7,6],8]]
# print(a[0][2],a[1][1],a[2][0],a[2][1][1],a[2][1][2],a[3][0],a[3][1][1],a[3][2])



# a=int(input("enter the number"))
# i=0
# b=[]
# while i<=a:
#     c=input("enter the number")
#     b.append(c)
#     i=i+1
# print(b)



# a=int(input("enter the number"))
# i=0
# b=[]
# d=[]
# d1=[]
# while i<=a:
#     c=int(input("enter the number"))
#     b.append(c)
#     if b[i]%2==0:
#         d.append(b[i])
#     else:
#         d1.append(b[i])
#     i=i+1
# print("Original List=",b)
# print("Even List=",d)
# print("Odd Number=",d1)



# a=[1,2,3,2,1,3,2,1,2]
# i=0
# b=[]
# while i<len(a):
#     if a[i] not in b:
#         b.append(a[i])
#     i=i+1
# print(b)



# a=[1,3,5,7,10]
# i=0
# b=[]
# while i<len(a)-1:
#     c=(a[i]+1)
#     b.append(c)
#     i=i+1
# d=b[3]+1
# b.append(d)
# print(b)



# a=[[2,3,[4,5],6],[3,4],[5,6,7],[8,4,3]]
# print(a[0][1],a[0][2][1],a[0][3],a[1][0],a[2][1],a[3][1],a[3][0])



# a="sky is blue"
# b=a.split()
# c=" "
# i=0
# while i<len(b):
#     b.reverse()
#     c=c+" "+b[i]
#     i=i+1
# print(c)




# Taking 'N' number of elements as input for an array 
# N = int(input("Enter the number of elements: ")) 
N=[2,4,2,5,6]
arr = [] 
 
for i in range(N): 
    element = int(input(f"Enter element {i+1}: ")) 
    arr.append(element) 
print("Input array:", arr) 