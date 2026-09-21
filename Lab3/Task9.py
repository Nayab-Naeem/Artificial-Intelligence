a = 0
b = 1

fib = []
while a<= 50:
    fib.append(a)
    a = b
    b = a+b
print (fib)

# Fizz buzz 1 to 50

for i in range (1,51):
    if i % 3 == 0 and i % 5 ==0:
        print ("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print ("Buzz")
    else:
        print (i)
