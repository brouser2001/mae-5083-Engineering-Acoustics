gamma={'air':1.4,'helium':1.66}
M={'air':0.02897,'helium':0.004}
Ru=8.3144
T_air=[295.37,243.71,505.37]
T_he=[310.37]

# a-d
for T in T_air:
    c=(gamma['air']*Ru*T/M['air'])**.5
    print(f'air, {T}-K, {c}-m/s, {c*2.23694}-mph')

# repeat for helium
for T in T_he:
    c=(gamma['helium']*Ru*T/M['helium'])**.5
    print(f'helium, {T}-K, {c}-m/s, {c*2.23694}-mph')

#e
T=T_air[0]
c=((gamma['air']*Ru*T/M['air'])**.5)*2.23694/3600 #miles/sec
print(f'c = {c} miles/sec')
print(f'in 5 seconds distance = {c*5} miles')