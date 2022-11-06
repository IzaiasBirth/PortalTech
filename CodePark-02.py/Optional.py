#definição da função que calcula a idade usando o ano entre 1922 e 2021 como parametro
def calcIdade(ano):
  #se o ano estiver dentro do intervalo, se diminui 2022 (ano atual) pelo ano digitado e salva o resultado na variavel res
  if ano >= 1922 and ano <= 2021:
    #a variavel res é opcional, podendo se digitar -> return 2022 - ano
    res = 2022 - ano
  #se o ano não estiver dentro do intervalo, com o raise Exception se cria uma mensagem de erro
  else:
    raise Exception("Ano digitado é fora do limite permitido.")
  #esse return tanto pode ficar aqui fora do if, quanto dentro dele
  return res

#recebe o nome da pessoa
nome = str(input("Qual seu nome? "))
#cria um laço infinito, podendo tambem se usar uma variavel de controle como while pararLaço == True ... while pararLaço == 0
while True:
  #esse primeiro try/except é responsável por testar se o ano de nascimento digitado é inteiro e não vazio, caso não for, vai pra o except na ultima linha
  try:
    anoNasc = int(input(f"Qual o ano que você nasceu, {nome}? (1922 até 2021) "))
    #esse segundo try/except é responsável por chamar a função calcIdade, onde o except recebe a mensagem de erro criada lá dentro da função com o raise
    try:
      #a variavel idade recebe o resultado da função calcIdade, repare que o parametro passado para a função é a variavel anoNasc
      idade = calcIdade(anoNasc)
      #uso o f no print antes das aspas, pra poder colocar as variaveis diretamente na frase, também é válido -> print(nome, ", você terá", idade, "anos em 2022")
      print(f"{nome}, você terá {idade} anos em 2022")
      #esse break é a condição de parada, podendo ser substituido pela mudança na variavel de controle como while pararLaço = False .. while pararLaço = 1
      break
    #esse é o except do segundo try, que usa o raise Exception da função como mensagem, o err que eu coloquei, é o nome que dei pro erro, pode ser qualquer um
    except Exception as err:
      print(err)
  #esse é o except do primeiro try que caso não seja digitado um inteiro ou vazio, ele é chamado    
  except:
    print("Digite um valor de entrada válido")