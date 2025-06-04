# Solicita uma frase
frase = input("Digite uma frase: ")

# Divide a frase em palavras e conta quantas são
quantidade = len(frase.split())

# Mostra o total de palavras
print(f"A frase contém {quantidade} palavras.")

# Quando você usa frase.split(), ele divide a string frase em partes sempre que encontra um espaço em branco 
# (ou qualquer outro delimitador que você especificar).
#  O resultado será uma lista de palavras ou substrings.
