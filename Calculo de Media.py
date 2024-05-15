login=input("Digite o seu login: ")
senha=input("Digite a sua senha: ")
if login == "userpy" or senha== "senha123":
    print("Seja bem vindo")
else:
    print("Login Falhou, tente novamente")

"****************************CALCULO**********************"

print ("Nota 1: ")
nota1 = input()

print("Nota 2: ")
nota2 = input()

soma = float(nota1) + float(nota2)
media = soma / 2

print (media)

if (media > 5 and media <=10):
    print("Você está Aprovado!")
elif (media > 3 and media < 6):
    print("Você está de Recuperação!")
elif (media >= 0 and media < 4):
    print("Você está Retido!")
else:
    print("Valor invalido")

input()