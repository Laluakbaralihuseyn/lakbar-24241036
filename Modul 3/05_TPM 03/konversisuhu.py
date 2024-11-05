def fahrenheit_ke_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Input suhu dari pengguna
f = float(input("Masukkan suhu dalam Fahrenheit: "))
celsius = fahrenheit_ke_celsius(f)

print(f"Suhu {f}°F setara dengan {celsius:.2f}°C")
