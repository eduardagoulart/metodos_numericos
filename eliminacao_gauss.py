from decimal import Decimal
def arquivo_matriz():
    file = open('input/matriz.txt','r')
    dimensao = int(file.readline().replace('\n', ''))
    matriz = []
    for linha in file.readlines():
        linha = linha.replace('\n','')
        coluna = list(map(int, linha.split(' ')))
        matriz.append(coluna)
    return dimensao, matriz


def arquivo_vetor():
    file = open('input/vetor.txt','r')
    vetor = file.readline().split(' ')
    return vetor


def triangulacao(matriz, dimensao):
    vetor_B = arquivo_vetor()
    for i in range(len(vetor_B)):
        vetor_B[i] = float(vetor_B[i])
    for i in range(0, dimensao - 1):
        for j in range(i+1, dimensao):
            multiplicador = matriz[j][i]/matriz[i][i]
            for k in range(0, dimensao):
                matriz[j][k] -= multiplicador * matriz[i][k]
            vetor_B[j] -= multiplicador*vetor_B[i]

    for i in range(0, dimensao-1):
        for j in range(0, dimensao):
            matriz[i][j] = round(matriz[i][j], 1)
            vetor_B[j] = round(vetor_B[j], 10)

    return matriz, vetor_B


def substitui(matriz_inicial, dimensao):
    matriz, vetor_B = triangulacao(matriz_inicial, dimensao)

    vetor_X = [vetor_B[i] for i in range(0, dimensao)]

    for i in range(dimensao-1, -1, -1):
        for j in range(i + 1, dimensao):
            vetor_X[i] -= matriz[i][j] * vetor_X[j]

        vetor_X[i] /= matriz[i][i]
    return vetor_X



if __name__ == "__main__":
    dimensao, matriz = arquivo_matriz()
    vetor_B = arquivo_vetor()

    print(substitui(matriz, dimensao))
