import math
a=int(input("cạnh thứ 1:"));
b=int(input("cạnh thứ 2:"));
c=int(input("cạnh thứ 3:"));
cv=a+b+c
p=cv/2
dt=math.sqrt(p*(p-a)*(p-b)*(p-c))
print("chu vi =", cv)
print("diện tích =", dt)