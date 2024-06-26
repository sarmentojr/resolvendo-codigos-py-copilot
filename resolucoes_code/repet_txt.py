#  Agora vamos solicitar uma string e um número inteiro como entrada. Depois teremos que retornar a string repetida o número de vezes informado.

string = input("Digite uma string: ")
numero_inteiro = int(input("Digite um número inteiro: "))
numero_repeticoes = 4

string_repetida = string * numero_repeticoes

print("String repetida:"," ", string_repetida)