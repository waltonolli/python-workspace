# Sal's Shipping

weight = 41

# Envio terrestre
if weight <= 2:
  price_per_pound = weight * 1.5
elif weight <= 6:
  price_per_pound = weight * 3.0
elif weight <= 10:
  price_per_pound = weight * 4.0
else:
  price_per_pound = weight * 4.75

shipping_rate = 20
print("Ground Shipping: $",price_per_pound + shipping_rate)

# Envio terrestre premium
shipping_rate_premium = 125.00
print("Ground Shipping Premium: $",shipping_rate_premium)

# Drone Shipping
if weight <= 2:
  price_per_pound = weight * 4.5
elif weight <= 6:
  price_per_pound = weight * 9.0
elif weight <= 10:
  price_per_pound = weight * 12.0
else:
  price_per_pound = weight * 14.75

print("Drone Shipping: $",price_per_pound)