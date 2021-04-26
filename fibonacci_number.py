#Basic Fibonacci number
a = 1
b = 0
length = int(input("Enter length: "))
i = 0
while i < length:
    print(b)
    b += a
    a = b-a
    i += 1

