while True:
    try:
        print('1: Soma\n2: Subtração\n3: Multiplicação\n4: Divisão\n0: Sair')
        op = float(input('Digite uma opção para calcular: '))
        if (op > 4):
            print('Essa opção não existe')
        elif (op == 0):
            break
        else:
            n1 = float(input('Digite o primeiro Número: '))
            n2 = float(input('Digite o segundo número: '))

            def calcular(n1, n2, op):
                if op == 1:
                    soma = n1 + n2
                    return soma
                elif op == 2:
                    sub = n1 -  n2
                    return sub
                elif op == 3:
                    mult = n1 * n2
                    return mult
                elif op == 4:
                    div = n1 / n2
                    return div
            print(f'O resultado é: {calcular(n1, n2, op)}')
    except:
        print('O dado informado não é válido; tente novamente')