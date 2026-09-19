print("=== MENU DE OPERAÇÕES ===")
print("1 - Soma (+)")
print("2 - Subtração (-)")
print("3 - Multiplicação (*)")
print("4 - Divisão (/)")

opcao = int(input("Escolha uma opção (1-4): "))

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("\n--- Resultado ---")

# Estrutura match/case em Python
match opcao:
    case 1:
        resultado = num1 + num2
        print(f"{num1} + {num2} = {resultado}")
    case 2:
        resultado = num1 - num2
        print(f"{num1} - {num2} = {resultado}")
    case 3:
        resultado = num1 * num2
        print(f"{num1} * {num2} = {resultado}")
    case 4:
        if num2 != 0:
            resultado = num1 / num2
            print(f"{num1} / {num2} = {resultado}")
        else:
            print("Erro: Divisão por zero não é permitida.")
    case _:
        print("Opção inválida!")


#Versão Portugol:

#        programa
#{
#	funcao inicio()
#	{
#		real num1, num2, resultado
#		inteiro opcao
#
#		escreva("=== MENU DE OPERAÇÕES ===\n")
#		escreva("1 - Soma (+)\n")
#		escreva("2 - Subtração (-)\n")
#		escreva("3 - Multiplicação (*)\n")
#		escreva("4 - Divisão (/)\n")
#		escreva("Escolha uma opção (1-4): ")
#		leia(opcao)
#
#		escreva("Digite o primeiro número: ")
#		leia(num1)
#		escreva("Digite o segundo número: ")
#		leia(num2)
#
#		escreva("\n--- Resultado ---\n")
#
#		// Estrutura escolha/caso (equivalente ao match/case)
#		escolha (opcao)
#		{
#			caso 1:
#				resultado = num1 + num2
#				escreva(num1, " + ", num2, " = ", resultado)
#				pare
#			caso 2:
#				resultado = num1 - num2
#				escreva(num1, " - ", num2, " = ", resultado)
#				pare
#			caso 3:
#				resultado = num1 * num2
#				escreva(num1, " * ", num2, " = ", resultado)
#				pare
#			caso 4:
#				se (num2 != 0) {
#					resultado = num1 / num2
#					escreva(num1, " / ", num2, " = ", resultado)
#				} senao {
#					escreva("Erro: Divisão por zero não é permitida.")
#				}
#				pare
#			caso contrario:
#				escreva("Opção inválida!")
#		}
#	}
#}