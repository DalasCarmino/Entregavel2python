soma = 0

# Leitura dos 5 números usando o laço for
for i in range(1, 6):
    numero = float(input(f"Digite o {i}º número: "))
    
    # Inicializa maior e menor na primeira repetição
    if i == 1:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
            
    soma += numero

media = soma / 5

print("\n--- Resultado ---")
print(f"Soma: {soma}")
print(f"Média: {media}")
print(f"Maior valor: {maior}")
print(f"Menor valor: {menor}")


#Versão portugol:

#programa
#{
#	funcao inicio()
#	{
#		real numero, soma, media, maior, menor
#		soma = 0.0
#
#		// Leitura do primeiro número fora do laço para inicializar maior e menor
#		escreva("Digite o 1º número: ")
#		leia(numero)
#		
#		soma = numero
#		maior = numero
#		menor = numero
#
#		// Laço de repetição para os outros 4 números
#		para (inteiro i = 2; i <= 5; i++)
#		{
#			escreva("Digite o ", i, "º número: ")
#			leia(numero)
#
#			soma = soma + numero
#
#			se (numero > maior) {
#				maior = numero
#			}
#
#			se (numero < menor) {
#				menor = numero
#			}
#		}
#
#		media = soma / 5
#
#		escreva("\n--- Resultado ---")
#		escreva("\nSoma: ", soma)
#		escreva("\nMédia: ", media)
#		escreva("\nMaior valor: ", maior)
#		escreva("\nMenor valor: ", menor)
#	}
#}