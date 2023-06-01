i=0
a=[]
while i<3:
    j=0
    b=[]
    while j<3:
        n=int(input("Enter the number"))
        b.append(n)
        j=j+1
    a.append(b)
    i=i+1
i=0
while i<3:
    j=0
    while j<3:
        print(a[i][j],end=" ")
        j=j+1
    print()
    i=i+1
S1=0
S2=0
i=0
while i<3:
    j=0
    while j<3:
        if i==j:
            S1=S1+a[i][j]
        if i+j==3-1:
            S2=S2+a[i][j]
        j=j+1
    i=i+1
if S1!=S2:
    f=1
else:
    i=0
    while i<3:
        SR=0
        SC=0
        j=0
        while j<3:
            SR=SR+a[i][j]
            SC=SC+a[i][j]
            j=j+1
        if SR!=S1:
            f=1
        elif SC!=S1:
            f=1
        else:
            f=0
        i=i+1
if f==0:
    print("Number is Magic square")
else:
    print("Number is not Magic square")