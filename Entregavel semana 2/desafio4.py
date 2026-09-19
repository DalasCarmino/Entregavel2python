SENHA_CORRETA = "1234"
tentativas = 0
MAX_TENTATIVAS = 3
autenticado = False

while tentativas < MAX_TENTATIVAS and not autenticado:
    senha_digitada = input("Digite a senha: ")
    tentativas += 1

    if senha_digitada == SENHA_CORRETA:
        autenticado = True
        print("\nAcesso concedido! Bem-vindo(a).")
    else:
        if tentativas < MAX_TENTATIVAS:
            print(f"Senha incorreta. Tentativa {tentativas} de {MAX_TENTATIVAS}.\n")

# Se saiu do laço sem autenticar
if not autenticado:
    print("\nNúmero máximo de tentativas atingido. Acesso BLOQUEADO!")


#programa
#{
#	funcao inicio()
#	{
#		cadeia senhaCorreta = "1234"
#		cadeia senhaDigitada
#		inteiro tentativas = 0
#		inteiro maxTentativas = 3
#		logico autenticado = falso
#
#		enquanto (tentativas < maxTentativas e nao autenticado)
#		{
#			escreva("Digite a senha: ")
#			leia(senhaDigitada)
#			
#			tentativas = tentativas + 1
#
#			se (senhaDigitada == senhaCorreta) {
#				autenticado = verdadeiro
#				escreva("\nAcesso concedido! Bem-vindo(a).\n")
#			} senao {
#				se (tentativas < maxTentativas) {
#					escreva("Senha incorreta. Tentativa ", tentativas, " de ", maxTentativas, ".\n\n")
#				}
#			}
#		}
#
#		// Se esgotou as tentativas e não autenticou
#		se (nao autenticado) {
#			escreva("\nNúmero máximo de tentativas atingido. Acesso BLOQUEADO!\n")
#		}
#	}
#}