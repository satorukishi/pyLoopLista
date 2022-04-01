# sintaxe do For
# for <variavel> in <iterator>
# Iterator é algo que você pode fazer o uso da iteração
# por exemplo, solicitar que o usuário digite vários números

lista = []
# range é o nosso iterator. Ele vai de 1 a 4 nesse exemplo, pois o 5 é exclusivo
for i in range(1, 5):
    lista.append(int(input("Digite o número " + str(i) + ": ")))

print(i)
print(lista)

# for sendo usado em uma Lista
for i in lista:
    print("O valor é: ", i)

