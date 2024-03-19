def inverter_abordagem1(cadeia):
    index = -1
    nova_cadeia = []
    for i in cadeia:
        nova_cadeia.append(cadeia[index])
        index -= 1
    return nova_cadeia

def inverter_abordagem2(cadeia):
    return cadeia[::-1]

cadeia = input("Escreva qual cadeia você deseja inverter: ")
print(*inverter_abordagem1(cadeia))
print(*inverter_abordagem2(cadeia))