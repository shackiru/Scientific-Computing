print("hello world")
print(20)
print(20.5)

# Guna dari (+) adalah untuk Concat
varName = "Shaquille " + "Ditama Putra"
num = 10


print("Sesuatu")

#Change Char to ASCII
print(ord('a'))

#Change ASCII to Char
print(chr(65))

#Print Format
print(f"Nama: {varName}, Number: {num}")

print(f"Nama: {varName}" + f", Number: {num}")

#Python gaada increment/decrement (++ atau --)
#Operator tambahan ** -> pangkat
#dan // -> pembagian yang dibulatkan

#Example

print(5//3)
print(format(5/3, ".2f"))
print(5**3)

#Selection & Repetition
a = 10
b = 10

if(a == 10):
    print("a itu = b")
elif(b > a):
    print("b > a")
else:
    print("a tidak sama dengan b")
    
print("luar")

#Parameter pertama untuk mulainya, kedua untuk jarak, 
#dan yang ketiga untuk lompatan
#for i in range(10, 0, -1):
    #print(i, end = " ")
    
#i= 10
#while i > 0:
    #print(format(i, ".1f"))z
    #i -= 0.1
    
#Function
def calculate(a, b):
    print("processing")
    plus = a + b
    minus = a - b
    times = a * b
    divide = a / b
    return plus, minus, times, divide

plus, minus, multi, divide = calculate(5, 3)

print(f"Pertambahan: {plus}", f"Pengurangan: {minus}")
print(f"Perkalian: {multi}", f"Pembagian: {divide}")
