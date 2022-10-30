num1 = float(input('Primeiro número: '))
op = int(input('Digite a operação (1 (soma), 2 (sub), 3 (mult), 4 (div)): '))
num2 = float(input('Segundo número: '))

def calcular(num1, num2, op):
    if op == 1:
        soma = num1 + num2
        return soma
    elif op == 2:
        sub = num1 - num2
        return sub
    elif op == 3:
        mult = num1 * num2
        return mult
    elif op == 4:
        div = num1 / num2
        return div
    else:
        return 0
print(calcular(num1, num2, op))


