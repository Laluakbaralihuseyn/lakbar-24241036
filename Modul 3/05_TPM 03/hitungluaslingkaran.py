import math

def luas_lingkaran(radius):
    return math.pi * radius ** 2

# Input radius dari pengguna
r = float(input("Masukkan radius lingkaran: "))
luas = luas_lingkaran(r)

print(f"Luas lingkaran dengan radius {r} adalah {luas:.2f}")
