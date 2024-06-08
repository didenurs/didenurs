# find roots of a polynomial

# import math

def possible_solutions(a,c):
    factors_of_c_array = []
    factors_of_a_array = []
    possible_solution_array = []
    for x in range(1, abs(c)+1):
        if c % x == 0:
            factors_of_c_array.append(x)
    for y in range(1, abs(a)+1):
        if a % y == 0:
            factors_of_a_array.append(y)
    for factor_c in factors_of_c_array:
        for factor_a in factors_of_a_array:
            possible_solution_array.append(factor_c / factor_a)
    for factor_c in factors_of_c_array:
        for factor_a in factors_of_a_array:
            possible_solution_array.append(-1 * factor_c / factor_a)
    return possible_solution_array


def roots_of_cubic(a, b, c, poss_solutions):
    solution_array = []
    for poss_solution in poss_solutions:
        cubic_value = a * pow(poss_solution, 2) + b * poss_solution + c
        if cubic_value == 0:
            solution_array.append(poss_solution)
    return solution_array

a = int(input("what is a:"))
b = int(input("what is b:"))
c = int(input("what is c:"))

poss_solutions = possible_solutions(a,c)
the_solutions = roots_of_cubic(a, b, c, poss_solutions)

print("The solutions of the polynamial are: \n")
for the_solution in the_solutions:
    print("x = " + str(the_solution) + " " + "\n")