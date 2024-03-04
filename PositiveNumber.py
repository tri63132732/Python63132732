
#Nhap 0<n<=1000
while True: 
    n = int(input("Nhap mot so bat ki (0<n<=1000): "))
    if n>0 and n<=1000:
        break
      

#Kiem tra mot so tu nhien la so nguyen to
def LaSNT(n):
    if n<2: return False
    for i in range (2, n//2 +1):
        if n%i ==0: return False
    return True    

#Kiem tra n la so nguyen to
if LaSNT(n):
    print("{} la so nguyen to".format(n))
else:
    print("{} khong la so nguyen to".format(n))    

#In so nguyen to <=n
print("Cac so nguyen to <={}".format(n))
for i in range(2,n+1):
    if(LaSNT(i)): print("%5d" %i, end=" ")
    