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

