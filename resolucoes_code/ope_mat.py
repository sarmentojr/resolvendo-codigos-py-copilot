# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite um número inteiro: "))

operacao = input("Digite a operação desejada (+, -, *, /): ")


if operacao == "+":
  resultado = numero1 + numero2
elif operacao == "-":
  resultado = numero1 - numero2
elif operacao == "*":
  resultado = numero1 * numero2
elif operacao == "/":
  resultado = numero1 / numero2
else:
  print("Operação inválida!")
  exit()


print("O resultado da operação é:", resultado)