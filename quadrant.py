x,y=map(int,list(input("Enter the values of x and y:").split()))
if x>0 and y>0:
    print(f"{x} and {y} lies in the first quadrant")
elif x<0 and y>0:
    print(f"{x} and {y} lies in the second quadrant")
elif x<0 and y<0:
    print(f"{x} and {y} lies in the third quadrant")
elif x>0 and y<0:
    print(f"{x} and {y} lies in the fourth quadrant")
elif x==0 and y==0:
    print(f"{x} and {y} lies at the origin")
elif y==0 and x!=0:
    print(f"{x} and {y} lies on x-axis")
elif x==0 and y!=0:
    print(f"{x} and {y} lies on y-axis")
else:
    print("Error")