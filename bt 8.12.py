
n=eval(input("nhập n:"))
kt=True
if n<2: kt =False
for i in range(2,n//2+1):
    if n%i==0: kt=False
if kt==True:
    print('là số ng tố')
else:
    print('ko là số ng tố')
