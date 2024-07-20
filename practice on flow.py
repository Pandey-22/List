# N=int(input("enter the element:-"))
# list=[40,30,20,45,50]
# list[N],i=0
# if i<N:
#     a=int(input("enter the number:-")) 
#     list[i]=a
#     i+=1
# m=list[0]
# i=1
# if i<N:
#     if list[i]<m:
#         m=list[i]
#         i+=1
#     print(m)   



# Take input from the user
year = int(input("Enter a year: "))

# Check if the year is a leap year and output the result
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Yes")
else:
    print("No")
