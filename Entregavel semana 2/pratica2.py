num1 = float(input("Digite o primeiro: "))
num2 = float(input("Digite o segunto número: ")) #Solicitação dos valores

print("/n--- MENU DE OPERAÇÕES ---")
print("1 - Soma")
print("2 - Substração")
print("3 - Multipliacão")
print("4 - Divisão") 

opcao = int(input("Escolha uma opção (1-4): ")) #Menu de operações, assim, o usuário poderá escolher qual das opções querer


match opcao:
    case 1:
        resultado = num1 + num2
        print(f"Resultado da Soma: {resultado}")
    case 2:
        resultado = num1 - num2
        print(f"Resultado da Subtração: {resultado}")
    case 3:
        resultado = num1 * num2
        print(f"Resultado da Multlipação: {resultado}")
    case 4:
        if num2 != 0:
            resultado = num1 / num2
            print(f"Resultado da Divisão: {resultado}")
        else:
            print(f"Erro: Não é possível dividir por zero!")
    case _:
        print("Opção inválida! Escolha um número entre 1 e 4") #Todas as operações disponíveis


#programa
#{
#	funcao inicio()
#	{
#		real num1, num2, resultado
#		inteiro opcao
#
#		// Entrada dos dois números
#		escreva("Digite o primeiro número: ")
#		leia(num1)
#
#		escreva("Digite o segundo número: ")
#		leia(num2)
#
#		// Exibição do menu
#		escreva("\n--- MENU DE OPERAÇÕES ---\n")
#		escreva("1 - Soma\n")
#		escreva("2 - Subtração\n")
#		escreva("3 - Multiplicação\n")
#		escreva("4 - Divisão\n")
#		escreva("Escolha uma opção (1-4): ")
#		leia(opcao)
#
#		// Estrutura escolha-caso
#		escolha (opcao)
#		{
#			caso 1:
#				resultado = num1 + num2
#				escreva("\nResultado da Soma: ", resultado)
#				pare
#			caso 2:
#				resultado = num1 - num2
#				escreva("\nResultado da Subtração: ", resultado)
#				pare
#			caso 3:
#				resultado = num1 * num2
#				escreva("\nResultado da Multiplicação: ", resultado)
#				pare
#			caso 4:
#				se (num2 != 0) {
#					resultado = num1 / num2
#					escreva("\nResultado da Divisão: ", resultado)
#				} senao {
#					escreva("\nErro: Não é possível dividir por zero!")
#				}
#				pare
#			caso contrario:
#				escreva("\nOpção inválida! Escolha um número entre 1 e 4.")
#		}
#	}
#}