# Inicialização da variável para a soma acumulada
soma = 0

# Laço FOR de 0 até 4 (total de 5 repetições)
for i in range(5):
    num = float(input(f"Digite o {i + 1}º número: "))
    
    # Acumula a soma
    soma += num
    
    # Na primeira repetição, define o primeiro número como maior e menor
    if i == 0:
        maior = num
        menor = num
    else:
        # Verifica se o número atual é maior que o salvo
        if num > maior:
            maior = num
        # Verifica se o número atual é menor que o salvo
        if num < menor:
            menor = num

# Cálculo da média
media = soma / 5

# Exibição dos resultados
print("\n--- RESULTADOS ---")
print(f"Soma:  {soma}")
print(f"Média: {media:.2f}")
print(f"Maior: {maior}")
print(f"Menor: {menor}")

#programa
#{
#	funcao inicio()
#	{
#		real num, soma, media, maior, menor
#		inteiro i
#
#		// Inicialização da soma com zero
#		soma = 0.0
#
#		// Laço para (FOR) de 1 até 5
#		para (i = 1; i <= 5; i++)
#		{
#			escreva("Digite o ", i, "º número: ")
#			leia(num)
#
#			// Acumula a soma
#			soma = soma + num
#
#			// Na primeira repetição, guarda o primeiro valor como maior e menor
#			se (i == 1) {
#				maior = num
#				menor = num
#			}
#			senao {
#				se (num > maior) {
#					maior = num
#				}
#				se (num < menor) {
#					menor = num
#				}
#			}
#		}
#
#		// Cálculo da média
#		media = soma / 5.0
#
#		// Exibição dos resultados
#		escreva("\n--- RESULTADOS ---\n")
#		escreva("Soma:  ", soma, "\n")
#		escreva("Média: ", media, "\n")
#		escreva("Maior: ", maior, "\n")
#		escreva("Menor: ", menor, "\n")
#	}
#}