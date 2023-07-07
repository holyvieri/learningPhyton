from fractions import Fraction
qntTeste = int(input())

for qnt in range(qntTeste):
    mathExpression = input().split()

    if "+" in mathExpression:
        n1s = int(mathExpression[0])
        d1s = int(mathExpression[2])
        n2s = int(mathExpression[4])
        d2s = int(mathExpression[6])
        sum_result = Fraction(n1s, d1s) + Fraction(n2s, d2s)
        if (sum_result.denominator == 1):
            sum_result = f'{sum_result.numerator}/1'
        print(f'{(n1s*d2s) + (n2s*d1s)}/{d1s*d2s} = {sum_result}')
    elif "-" in mathExpression:
        n1t = int(mathExpression[0])
        d1t = int(mathExpression[2])
        n2t = int(mathExpression[4])
        d2t = int(mathExpression[6])
        sub_result = Fraction(n1t, d1t) - Fraction(n2t, d2t)
        if (sub_result.denominator == 1):
            sub_result = f'{sub_result.numerator}/1'
        print(f'{(n1t*d2t) - (n2t*d1t)}/{d1t*d2t} = {sub_result}')
    elif "*" in mathExpression:
        n1m = int(mathExpression[0])
        d1m = int(mathExpression[2])
        n2m = int(mathExpression[4])
        d2m = int(mathExpression[6])
        multi_result = Fraction(n1m, d1m) * Fraction(n2m, d2m)
        if (multi_result.denominator == 1):
            multi_result = f'{multi_result.numerator}/1'
        print(f'{n1m*n2m}/{d1m*d2m} = {multi_result}')
    else:
        n1d = int(mathExpression[0])
        d1d = int(mathExpression[2])
        n2d = int(mathExpression[4])
        d2d = int(mathExpression[6])
        div_result = Fraction(n1d, d1d) / Fraction(n2d, d2d)
        if (div_result.denominator == 1):
            div_result = f'{div_result.numerator}/1'
        print(f'{n1d*d2d}/{n2d*d1d} = {div_result}')
