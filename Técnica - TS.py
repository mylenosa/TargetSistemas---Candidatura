"""
Mylena Viana Nunes - 10/09/24
"""

# Questão 1
def pertence_fibonacci(num):
    fibonacci = [0, 1]
    while fibonacci[-1] < num:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    if num in fibonacci:
        return f"O numero {num} pertence a sequencia de Fibonacci."
    else:
        return f"O numero {num} NÃO pertence a sequencia de Fibonacci."

numero = int(input("Informe um numero: "))
print(pertence_fibonacci(numero))


# Questão 2
def conta_letra_a(texto):
    texto = texto.lower()
    contagem = texto.count('a')
    
    if contagem > 0:
        return f"A letra 'a' ocorre {contagem}x na string."
    else:
        return "A letra 'a' não ocorre na string."


string = input("Informe uma string: ")
print(conta_letra_a(string))


# Questão 3
INDICE = 12
SOMA = 0
K = 1

while K < INDICE:
    K = K + 1
    SOMA = SOMA + K

print(f"Valor de SOMA: {SOMA}")


# Questão 4
# a)
def proximo_impar(ultima):
    return ultima + 2

ultima = 7
print("Proximo numero impar:", proximo_impar(ultima))

# b)
def proximo_dobro(ultimo):
    return ultimo * 2

ultimo = 64
print("Proximo numero na sequencia:", proximo_dobro(ultimo))

# c) 
def proximo_quadrado(n):
    return (n + 1) ** 2

ultimo = 36
print("Proximo numero na sequencia dos quadrados perfeitos:", proximo_quadrado(int(ultimo ** 0.5)))

# d)
def proximo_quadrado_par(n):
    return (n + 2) ** 2

ultimo = 64
ultimo_par = int(ultimo ** 0.5)  
print("Proximo numero na sequencia dos quadrados de numeros pares:", proximo_quadrado_par(ultimo_par))

# e)
def proximo_fibonacci(a, b):
    return a + b

ultimo1, ultimo2 = 5, 8
print("Proximo numero na sequencia de Fibonacci:", proximo_fibonacci(ultimo1, ultimo2))

# f)
def proximo_numero(ultimo):
    return ultimo + 1

ultimo = 19
print("Proximo numero na sequencia:", proximo_numero(ultimo))


# Questão 5
import time

def identificar_interruptores():
    print("Ligue o primeiro interruptor e espere 5 minutos.")
    time.sleep(5 * 60)
    print("Desligue o primeiro interruptor e ligue o segundo interruptor.")
    time.sleep(1)
    print("Desligue o segundo interruptor e va para a sala das lampadas.")
    
    return {
        "Lâmpada 1": "Quente e apagada (Primeiro interruptor)",
        "Lâmpada 2": "Acesa (Segundo interruptor)",
        "Lâmpada 3": "Fria e apagada (Terceiro interruptor)"
    }

resultados = identificar_interruptores()
for lampada, status in resultados.items():
    print(f"{lampada} esta {status}.")