
a=eval(input("nhập loại xe:"))
b=eval(input("nhập số km:"))
c=eval(input("nhập thời gian chờ:"))
if(c<5):
     tiencho=0 
elif(c>=6):
     tiencho=c*800
print("Tiền chờ:",tiencho)
sotien=0
if(a==4):
   if(b<=20):
        sotien=12100*b
   elif(b>=21):
        sotien=10000*b
if(a==7):
   if(b<30):
        sotien=14100*b 
   elif(b>=31):
        sotien=12000*b
print("Tiền di chuyển:", sotien)
tiencuoc= tiencho + sotien
print("Tiền cước:", tiencuoc)  