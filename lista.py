"""
# Como calcular a média sem usar lista
numDigitado1 = int(input("Digite o 1o número: "))
numDigitado2 = int(input("Digite o 2o número: "))
numDigitado3 = int(input("Digite o 3o número: "))
numDigitado4 = int(input("Digite o 4o número: "))
numDigitado5 = int(input("Digite o 5o número: "))

resultado = (numDigitado1 + numDigitado2 + numDigitado3 + numDigitado4 + numDigitado5) / 5
print("A média é: ", resultado)
"""

# Declaração de uma lista vazia
lista = []

lista.append(int(input("Digite um número: ")))
lista.append(int(input("Digite um número: ")))
lista.append(int(input("Digite um número: ")))
lista.append(int(input("Digite um número: ")))
lista.append(int(input("Digite um número: ")))

print(lista) #[5, 7, 1, 3, 10]
    #  indice [0, 1, 2, 3, 4]


print(lista[2])
print(lista[6]) # aqui dá erro IndexError: list index out of range


# Inicializar a lista com valores
from random import randint

# A lista permite armazenar tipos diferentes de variáveis
lista = [False, "Satoru", 1, "11 98763-2222", 20.1]
print(lista)

aleatorio = randint(0, len(lista) - 1)
print("Valor aleatório da lista: ", lista[aleatorio])

# A lista só ordena lista se os tipos forem os mesmos
lista = ["Satoru", "Dericky", "Kishi", "Fumabare"]
lista.sort() # ordem crescente
print(lista) # ['Dericky', 'Fumabare', 'Kishi', 'Satoru']

lista.sort(reverse=True) #ordem decrescente
print(lista) # ['Satoru', 'Kishi', 'Fumabare', 'Dericky']

# insert serve para adicionar um item novo na posição passada como parâmetro
lista.insert(0, "Rico")
print(lista)

# Substitui o valor de uma lista
lista[1] = "Buzz"
print(lista)


