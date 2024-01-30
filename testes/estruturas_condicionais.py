MAIOR_IDADE = 18
IDADE_ESPECIAL = 17
idade = int(input("informe a sua idade: "))

if idade >= MAIOR_IDADE:
    print("pode tirar habilitação")

elif idade == IDADE_ESPECIAL:
    print("Pode fazer apenas aula teórica.")

else:
    print("Não pode tirar")