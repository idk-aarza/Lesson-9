#Take the input of the units for electricity 
aarza=int(input('No. of units consumed for electricity'))
if (aarza <50):
    amount=aarza*2.60
    subcharge=25
elif (aarza <=100):
    amount=130+((aarza-50)*3.25)
    subcharge=35
elif (aarza <=200):
    amount=130+162.50+((aarza-100)*5.26)
    subcharge=45
else:
    amount=130+162.50+526+((aarza-200)*8.45)
    subcharge=75
    
total=amount+subcharge
print("\nThe total electricity bill is=%.2f" %total)
    