# alu_price_per_kg = 56
# alu_kinchi = 4

# goru_price = 760
# goru_kinchi = 2

# alur_moot = alu_price_per_kg * alu_kinchi
# goru_moot = goru_price * goru_kinchi

# print(alur_moot)
# print(goru_moot)
# print(alur_moot + goru_moot)


van_alu = 40
swapno_alu = 57

van_tormoj = 340
swapno_tormoj = 323

van_moot = van_alu + van_tormoj
swapno_moot = swapno_alu + swapno_tormoj

# print(van_moot <= swapno_moot)

if van_moot < swapno_moot:
    print(f"Apni van theke kinte paren. Tahole apnar {swapno_moot - van_moot} taka laab hobe!")
elif van_moot > swapno_moot:
    print(f"Apni swapno theke kinte paren. Tahole apnar {van_moot - swapno_moot} taka laab hobe!")
else:
    print("Dekhen ja valo mone koren")
    

print("Thank you for choosing our service")