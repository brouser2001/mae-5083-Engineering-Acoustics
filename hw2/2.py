components = {
    'Nitrogen': {'percentage': 78.084, 'molecular_weight': 28.0134},
    'Oxygen': {'percentage': 20.948, 'molecular_weight': 31.9988},
    'Argon': {'percentage': 0.934, 'molecular_weight': 39.948},
    'Carbon Dioxide': {'percentage': 0.031, 'molecular_weight': 44.010}
}

result=0
for component in components.values():
    result+=0.01*component['percentage']*component['molecular_weight']
print(f'molecular weight of air = {result} - g/mol')

#b
Ru=8.3144
r_assumed=287.06 #J/kg∙K
r_calculated=Ru/(result*0.001)
print(f'Calculated value = {r_calculated} - ')
print(f'Difference = {r_assumed-r_calculated}')