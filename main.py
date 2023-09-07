print("¡Bienvenido a Python Pizza!")
size = input("¿Qué tamaño de pizza quieres? pequeño, mediano o grande\n ")
add_pepperoni = input("¿Quieres pepperoni (+2$ pequeño y +3$ mediano y grande)? si o no\n ")
extra_cheese = input("¿Quieres queso extra (+1 $)? si o no\n ")

price = 0
if size == "pequeño":
  price += 15
elif size == "mediano":
  price += 20
elif size == "grande":
  price += 25

# extra_pepperoni +2$ for S and +3$ for M and L   
if add_pepperoni == "si":
  if size == "pequeño":
    price += 2
  else:
    price += 3
else:
  (f"Su factura total es ${price}")
  
# extra_cheese +1$
if extra_cheese == "si":
  price += 1

print(f"Eligio una pizza pizza {size}. {add_pepperoni} para pepperoni y {extra_cheese} para extra queso.\n")
print(f"Su factura total es ${price}") 