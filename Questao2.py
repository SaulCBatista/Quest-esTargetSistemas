def numero_esta_sequecia_fibonacci(numero):
    if numero in calcular_fibonacci(numero):
        return "Número informado PERTENCE a sequência de Fibonacci!"
    else:
        return "Número informado NÃO PERTENCE a sequência de Fibonacci!"

def calcular_fibonacci(numero):
    if numero <= 0:
        return []
    elif numero == 1:
        return [0, 1]
    elif numero == 2:
        return [0, 1, 1, 2]
    elif numero >= 2:
       sequencia = calcular_fibonacci(numero - 1)
       proximo_numero = sequencia[-1] + sequencia[-2]
       sequencia.append(proximo_numero)
       return sequencia
    
numero = int(input("Informe o número que deseja verificar: "))
print(numero_esta_sequecia_fibonacci(numero))
