# 1. Перша умова
eq_1 = 17
eq_2 = 5 + 12
eq_3 = eq_1

print(eq_1, eq_2, eq_3)
print(id(eq_1), id(eq_2), id(eq_3))
print(type(eq_1), type(eq_2), type(eq_3))

# 2. Друга умова
dif_1 = '71'
dif_2 = str(71)

print(dif_1, dif_2)
print(id(dif_1), id(dif_2))
print(type(dif_1), type(dif_2))

# 3. Перетворення типів згідно завдання

new_eq_1 = str(eq_1)
new_eq_2 = str(3 + 14)
new_eq_3 = str(eq_3)

print(new_eq_3, new_eq_2, new_eq_3)
print(id(new_eq_1), id(new_eq_2), id(new_eq_3))
print(type(new_eq_1), type(new_eq_2), type(new_eq_3))

new_dif_1 = bool('71')
new_dif_2 = bool(str(71))

print(new_dif_1, new_dif_2)
print(id(new_dif_1), id(new_dif_2))
print(type(new_dif_1), type(new_dif_2))
