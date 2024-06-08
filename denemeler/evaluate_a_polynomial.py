#evaluate a polynomial

def EvaluatePolynomial(coef,x):
    if len(coef) == 0:
        return 0
    else:
        return coef[0] * x**(len(coef)-1) + EvaluatePolynomial(coef[1:],x)

coef = [3,2,1,0]
print(EvaluatePolynomial(coef,2))