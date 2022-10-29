# Laço que imprime andares de um prédio com exceção do 13º andar
andar = 1
for i in range(andar, 21):
    if i == 13:
        continue
    print(f'{i}º Andar')