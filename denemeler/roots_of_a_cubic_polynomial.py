# find roots of a cubic polynomial

# import math

def possible_solutions(a,d):
    factors_of_d_array = []
    factors_of_a_array = []
    possible_solution_array = []
    for x in range(1, abs(d)+1):
        if d % x == 0:
            factors_of_d_array.append(x)
    for y in range(1, abs(a)+1):
        if a % y == 0:
            factors_of_a_array.append(y)
    for factor_d in factors_of_d_array:
        for factor_a in factors_of_a_array:
            possible_solution_array.append(factor_d / factor_a)
    for factor_d in factors_of_d_array:
        for factor_a in factors_of_a_array:
            possible_solution_array.append(-1 * factor_d / factor_a)
    return possible_solution_array


def roots_of_cubic(a, b, c, d, poss_solutions):
    solution_array = []
    for poss_solution in poss_solutions:
        cubic_value = a * pow(poss_solution, 3) + b * pow(poss_solution, 2) + c * poss_solution + d
        if cubic_value == 0:
            solution_array.append(poss_solution)
    return solution_array

a = int(input("what is a:"))
b = int(input("what is b:"))
c = int(input("what is c:"))
d = int(input("what is d:"))

poss_solutions = possible_solutions(a,d)
the_solutions = roots_of_cubic(a, b, c, d, poss_solutions)

print("The solutions of the cubic are: \n")
for the_solution in the_solutions:
    print("x = " + str(the_solution) + " " + "\n")