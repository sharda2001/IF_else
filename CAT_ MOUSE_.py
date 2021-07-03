catA=int(input("enter the catA position"))
catB=int(input("enter the catB position"))
mouseC=int(input("enter the mouseC position"))
a=catA-mouseC
if a<0:
    a=a*-1
b=catB-mouseC
if b<0:
    b=b*-1
if catB==0:
    print("catB is winner")
elif a==b:
    print("mouseC is winner")
elif a>b:
    print("catB is  winner")
else:
    print("catA is winner")