
a=eval(input("nhập loại phòng:"))
b=eval(input("nhập số đêm:"))
if (a==1):
    st=1260000
elif(a==2):
    st=1550000
elif(a<5):
    st=1830000
elif(a<7):
    st=2120000
elif(a==7):
    st=2540000
elif(a==8):
    st=4800000
if (b==1):
    tt=st
elif(b<4):
    tt=(st-st*0.25)*b
else:
    tt=(st-st*0.3)*b
print("thành tiền:",tt)
