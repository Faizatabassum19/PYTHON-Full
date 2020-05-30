hrs = input("Enter Hours:")
h = float(hrs)
perhour = input("Enter rate:")
try:
    h= float(hrs)
    ph= float(perhour)
except:
    print("Not a number")
if(h>40):
    gp=(40*ph)+((h-40)*1.5*ph)
else:
    gp=h*ph
print(gp)
