a = int(input("enter the number="))
for i in range(2, a):
    if (a % i) == 0:
        print(a)
        print("it is not prime number")
        break
    else:
        print("Is a prime number")
        break

