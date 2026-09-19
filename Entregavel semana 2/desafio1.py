# Entrada de dados
idade = int(input("Digite a idade do cliente: "))
renda = float(input("Digite a renda do cliente: "))

print("\n--- Resultado ---")
print(f"Idade: {idade} anos")

# Classificação baseada na renda usando if, elif e else
if renda <= 2000:
    categoria = "Bronze"
elif renda <= 5000:
    categoria = "Prata"
elif renda <= 10000:
    categoria = "Ouro"
else:
    categoria = "Diamante"

print(f"Categoria: {categoria}")



#Versão em portugol:

# programa
#{
#	funcao inicio()
#	{
#		inteiro idade
#		real renda
#
#		escreva("Digite a idade do cliente: ")
#		leia(idade)
#
#		escreva("Digite a renda do cliente: ")
#		leia(renda)
#
#		escreva("\n--- Resultado ---")
#		escreva("\nIdade: ", idade, " anos")
#
#		// Classificação baseada na renda usando if/elif/else (se/senao se/senao)
#		se (renda <= 2000) {
#			escreva("\nCategoria: Bronze")
#		}
#		senao se (renda <= 5000) {
#			escreva("\nCategoria: Prata")
#		}
#		senao se (renda <= 10000) {
#			escreva("\nCategoria: Ouro")
#		}
#		senao {
#			escreva("\nCategoria: Diamante")
#		}
#	}
#}