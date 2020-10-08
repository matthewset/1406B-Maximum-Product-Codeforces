for i in range(int(input())):
    n=int(input())
    no=sorted(map(int,input().split(" ")))
    productone=no[0]*no[1]*no[n-1]*no[n-2]*no[n-3]#2 smallest * 3 biggest
    producttwo=no[0]*no[1]*no[2]*no[3]*no[n-1]#4 smallest * 1 biggest
    productthree=no[n-1]*no[n-2]*no[n-3]*no[n-4]*no[n-5]#5 biggest
    print(max(productone,producttwo,productthree))#maximum of these three
    
