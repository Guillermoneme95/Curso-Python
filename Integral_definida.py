def sum_riemman(f,a,b,dx):
    i=0
    sum=0
    while(dx*i<=b-a):
        sum=f*(a+dx*i)
        i+=1
    float(sum)
    print(sum)
    return sum
f=float(input("ingrese el valor de su función"))
a=float(input("ingrese el valor del limite inferior"))
b=float(input("ingrese el valor del limite superior"))
dx=float(input("ingrese el valor del intervalo"))
while(dx<=0):
    print("ingrese un valor distinto de cero")
    dx = float(input("ingrese el valor del intervalo"))
sum_riemman(f,a,b,dx)
