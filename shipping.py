weight = 10

#Ground Shipping

if weight <= 2 and weight > 0:
  cost = weight * 1.50 + 20.00
  
elif weight > 2 and weight <= 6:
  cost = weight * 3.00 + 20.00
 
elif weight > 6 and weight <= 10:
  cost = weight * 4.00 + 20.00
  
else:
  cost = weight * 4.75 + 20.00
  

print("Ground Shipping $", cost)

#premium price

cost_premium = 125
print("Ground Shipping Premium $",cost_premium)

#drone shipping
if weight <= 2 and weight > 0:
  cost = weight * 4.50 
  
elif weight > 2 and weight <= 6:
  cost = weight * 9.00
  
elif weight > 6 and weight <= 10:
  cost = weight * 12.00
  
else:
  cost = weight * 14.25
  

print("Drone Shipping $", cost)