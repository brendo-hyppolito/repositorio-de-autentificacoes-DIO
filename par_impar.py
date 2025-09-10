# Função que verifica se o número é par ou ímpar
def verificar_par_ou_impar():
    # Receber o número
    numero = int(input("Digite um número inteiro: "))
    
    # Verificar se o número é par ou ímpar
    if numero % 2 == 0:
        print(f"O número {numero} é par.")
    else:
        print(f"O número {numero} é ímpar.")

# Chamar a função
verificar_par_ou_impar()