Patm=1.01325

def Cwater(p,t):
    return 1402.7+488*t-482*t**2+135*t**3+(15.9+2.8*t+2.4*t**2)*(p-Patm)/100

#a
T=30/100
P=Patm
print(Cwater(P,T))


print((15.9+2.8*T+2.4*T**2)/100)