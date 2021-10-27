input_number = int(input("enter the number"))

is_prime = True

for number in range(2, int(input_number/2)+1):
    if input_number % number == 0:
        is_prime = False
        break

print(is_prime)


text = " i like coding in python the best "
part = text.replace("coding","program")
print(part)