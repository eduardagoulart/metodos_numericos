import time
# Lê o arquivo com a matriz
def arquivo_matriz():
    file = open('input/matriz.txt','r')
    dimensao = int(file.readline().replace('\n', ''))
    matriz = []
    for linha in file.readlines():
        linha = linha.replace('\n','')
        coluna = list(map(int, linha.split(' ')))
        matriz.append(coluna)
    return dimensao, matriz


# Lê o arquivo com o vetor
def arquivo_vetor():
    file = open('input/vetor.txt','r')
    vetor = file.readline().split(' ')
    return vetor


# Inicia o método de elimicação de Gauss
def triangulacao(matriz, dimensao, vetor_b):
    for i in range(0, dimensao - 1):
        for j in range(i+1, dimensao):
            multiplicador = matriz[j][i]/matriz[i][i]
            for k in range(0, dimensao):
                matriz[j][k] -= multiplicador * matriz[i][k]
            vetor_b[j] -= multiplicador*vetor_b[i]
    return matriz, vetor_b


def substitui(matriz_inicial, dimensao, vetor_b):
    matriz, vetor_b = triangulacao(matriz_inicial, dimensao, vetor_b)
    vetor_x = [vetor_b[i] for i in range(0, dimensao)]

    for i in range(dimensao-1, -1, -1):
        for j in range(i + 1, dimensao):
            vetor_x[i] -= matriz[i][j] * vetor_x[j]

        vetor_x[i] /= matriz[i][i]
    return vetor_x

# Finaliza a eliminação de Gauss


def gauss_seidel(matriz, vetor_b, dimensao, chute_inicial, iteracoes):
    x_anterior = [0.0 for i in range(dimensao)]
    for i in range(iteracoes):
        for j in range(dimensao):
            x_anterior[j] = chute_inicial[j]
        for j in range(dimensao):
            soma = 0.0
            for k in range(dimensao):
                if k != j:
                    soma += matriz[j][k] * chute_inicial[k]
            chute_inicial[j] = (vetor_b[j] - soma) / matriz[j][j]
        dif_norma = 0.0
        norma_anterior = 0.0
        for j in range(dimensao):
            dif_norma = dif_norma + abs(chute_inicial[j] - x_anterior[j])
            norma_anterior = norma_anterior + abs(x_anterior[j])
        if norma_anterior == 0.0:
            norma_anterior = 1.0
        norma = dif_norma / norma_anterior
        if (norma < iteracoes) and i != 0:
            print("A sequencia converge para [", end="")
            for j in range(dimensao - 1):
                print(chute_inicial[j], ",", end="")
            print(f'{chute_inicial[dimensao - 1]}]. Gastou {i+1} iterações')
            print(norma)
            return

    print("A matriz não converge.")


def menu():
    dimensao, matriz = arquivo_matriz()
    vetor_b = arquivo_vetor()
    for i in range(len(vetor_b)):
        vetor_b[i] = float(vetor_b[i])

    escolha = int(input("1. Gauss \n2. Gauss Seidel \n3. Sair\n"))
    if escolha == 1:
        inicio_gauss = time.time()
        print(substitui(matriz, dimensao, vetor_b))
        fim_gauss = time.time()
        print(f'Tempo gasto pela Eliminação de Gauss foi: {fim_gauss - inicio_gauss}')
    if escolha == 2:
        inicio_gauss_seidel = time.time()
        chute = dimensao * [0]
        iteracao = int(input("Digite a quantidade de iterações: "))
        print(gauss_seidel(matriz, vetor_b, dimensao, chute, iteracao))
        fim_gauss_seidel = time.time()
        print(f'O tempo gasto pelo método de Gauss Seidel foi: {fim_gauss_seidel - inicio_gauss_seidel}')
    if escolha == 3:
        return
    menu()


if __name__ == "__main__":
    print(menu())