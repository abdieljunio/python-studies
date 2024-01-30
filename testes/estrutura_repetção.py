texto = " "
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end =" ")


print() #add qubra de linha




for numero in range(0, 51, 5):
    print(numero, end = " -> ")