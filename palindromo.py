# Função que verifica se a palavra é um palíndromo
def verificar_palindromo():
    # Receber a palavra
    palavra = input("Digite uma palavra: ").strip().lower()  # remove espaços e converte para minúsculas
    
    # Verificar se a palavra é igual à sua versão invertida
    if palavra == palavra[::-1]:
        print(f"A palavra '{palavra}' é um palíndromo!")
    else:
        print(f"A palavra '{palavra}' não é um palíndromo.")

# Chamar a função
verificar_palindromo()
