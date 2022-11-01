from datetime import date
current_date = date.today()
data = current_date.year
nome = str(input('Digite seu nome completo: '))
contador = 0
while contador == 0:
    try:
        ano_nascimento = int(input('Digite o ano em que você nasceu (1922 - 2021): '))
        idade = data-ano_nascimento
    except:
        print("O dado inserido não é válido")
        continue
    if (ano_nascimento < 1922 or ano_nascimento > 2021):
            print('O ano informado não está correto')
    else:
        print(f"{nome}\n{idade} anos em {data}")
        exit()