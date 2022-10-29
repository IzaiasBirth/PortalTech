#CodePark - Atividade 2
quantRodas = int(input('Digite a quantidade de rodas do veículo: '))
peso = float(input('Digite o peso do veículo em quilogramas: '))
quantPessoas = int(input('Digite a quantidade de pessoas suportada do veículo: '))

if(quantRodas <= 3):
    print('Categoria A')
elif(quantRodas >= 4 and quantPessoas <= 8 and peso <= 3500):
    print('Categoria B')
elif(quantRodas >= 4 and peso >= 3500 and peso <= 6000):
    print('Categoria C')
elif(quantRodas >= 4 and quantPessoas > 8):
    print('Categoria D')
else:
    print('Categoria F')

#Alteração para teste
