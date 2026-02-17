number_one = int(input("Enter the first number: "))
number_two = int(input("Enter the second number: "))


for i in range(0, number_one):
    if i * number_two == number_one:
        print(f"The {number_one} id multiple of {number_two} for {i}")
        print(f"{number_two} X {i} = {number_one}")
