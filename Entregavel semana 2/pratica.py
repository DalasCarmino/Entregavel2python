idade = int(input("Digite a idade do cliente: "))
renda = float(input("Digite a renda menstal do cliente (R$): ")) #Solitação da idade do usuário

if renda >= 10000:
    categoria = "Diamante"
elif renda >= 5000 or (idade >= 60 and renda >= 3000):
    categoria = "Ouro"
elif renda >= 2500 or (idade >= 30 and renda >= 2000):
    categoria = "Prata"
else:
    categoria = "Bronze" #Verifiação do valor e categorização

print(f"Classificação do cliente: {categoria}")


#programa
#{
#	funcao inicio()
#	{
#		// Declaração de variáveis
#		inteiro idade
#		real renda
#		cadeia categoria
#
#		// Entrada de dados
#		escreva("Digite a idade do cliente: ")
#		leia(idade)
#
#		escreva("Digite a renda mensal do cliente (R$): ")
#		leia(renda)
#
#		// Estrutura condicional se / senao se / senao
#		se (renda >= 10000) {
#			categoria = "Diamante"
#		}
#		senao se (renda >= 5000 ou (idade >= 60 e renda >= 3000)) {
#			categoria = "Ouro"
#		}
#		senao se (renda >= 2500 ou (idade >= 30 e renda >= 2000)) {
#			categoria = "Prata"
#		}
#		senao {
#			categoria = "Bronze"
#		}
#
#		// Exibição do resultado
#		escreva("\nClassificação do cliente: ", categoria)
#	}
#}