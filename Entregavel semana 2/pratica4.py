SENHA_CORRETA = "1234"
limite_tentativas = 3
tentativas = 0

senha_digitada = input("Digite sua senha: ")
tentativas += 1

# Repete enquanto a senha estiver errada e ainda houver tentativas disponíveis
while senha_digitada != SENHA_CORRETA and tentativas < limite_tentativas:
    erros_restantes = limite_tentativas - tentativas
    print(f"Senha incorreta! Você ainda tem {erros_restantes} tentativa(s).")
    senha_digitada = input("Digite a senha novamente: ")
    tentativas += 1

# Verificação final
if senha_digitada == SENHA_CORRETA:
    print("Acesso permitido! Seja bem-vindo.")
else:
    print("Cartão/Conta bloqueada! Você excedeu o limite de 3 tentativas.")