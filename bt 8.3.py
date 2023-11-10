
a=eval(input("nhập a:"))
b=eval(input("nhập b:"))
if a==0:
    if b==0:
        print("phương trình vô số nghiệm")
    else:
        print("phương trình vô nghiệm")
else:
    x=-b/a
    print("nghiệm x =",x)