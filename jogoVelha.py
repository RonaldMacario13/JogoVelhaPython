def mostrar_quadro(quadro):
    for linha in quadro:
        print("|".join(linha))


def criar_quadro():
    quadro_linha = [["_", "_", "_"], ["_", "_", "_"], [" ", " ", " "]]
    mostrar_quadro(quadro_linha)
    return(quadro_linha)

# def atualizar_quadro(quadro_atualizado):
#     for linha in quadro_atualizado:
#         print("|".join(linha))

def jogada(pos_i, pos_j, jogador = 'x'):
    global quadro
    if quadro [pos_i][pos_j] in ['_', ' ']:
        quadro [pos_i][pos_j] = jogador
        mostrar_quadro(quadro)
        return True
    else:
        print("Posição está ocupada! Tente novamente.")
        return False

def verifcar_vencendor():
    global quadro

    for i in range(3):
        if quadro[i][2] in ['x', 'o'] and quadro[i][0] == quadro[i][1] == quadro[i][2]:
            print(f"jogador {quadro[i][0]} venceu!")
            return True

        if quadro[2][i] in ['x', 'o'] and quadro[0][i] == quadro[1][i] == quadro[2][i]:
            print(f"jogador {quadro[0][i]} venceu!")
            return True
    if quadro[0][0] in ['x', 'o'] and quadro[0][0] == quadro[1][1] == quadro[2][2]:
            print(f"jogador {quadro[0][0]} venceu!")
            return True
    if quadro[0][2] in ['x', 'o'] and quadro[0][2] == quadro[1][1] == quadro[2][0]:
            print(f"jogador {quadro[0][2]} venceu!")
            return True
    else:
         return False

def receber_jogada(jogador):
    status = False
    while not status:
        print(f"Jogador: {jogador}")
        linha = int(input("Digite a linha: "))
        coluna = int(input("Digite a coluna: "))
        status = jogada(linha, coluna, jogador)
    print("Jogada realizada!!")

