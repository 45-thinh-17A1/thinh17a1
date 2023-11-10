
import math
a=eval(input("nhập a:"))
b=eval(input("nhập b:"))
c=eval(input("nhập c:"))
p=(a+b+c)/2
dt=math.sqrt(p*(p-a)*(p-b)*(p-c))
print("diện tích =",dt)