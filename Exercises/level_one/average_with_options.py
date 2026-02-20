# Desenvolva um algoritmo que permita ao usuário calcular a média ponderada e harmônica de três notas.

calculate = input("Enter either 'w' for weighted or 'h' for harmonic: ")
if calculate == "w":
    grade1 = float(input("Enter the first grade: "))
    weight1 = float(input("Enter the weight for the first grade: "))
    grade2 = float(input("Enter the second grade: "))
    weight2 = float(input("Enter the weight for the second grade: "))
    grade3 = float(input("Enter the third grade: "))
    weight3 = float(input("Enter the weight for the third grade: "))

    weighted_average = (grade1 * weight1 + grade2 * weight2 + grade3 * weight3) / (
        weight1 + weight2 + weight3
    )
    print(f"The weighted average is: {weighted_average}")
